import re
import os
import tempfile
import requests
import yt_dlp


class SubtitleService:
    @staticmethod
    def extract_subtitles(video_url: str) -> tuple[str, str]:
        """
        Extract subtitles from a YouTube video URL.

        Args:
            video_url: URL of the YouTube video

        Returns:
            tuple: (subtitle_text, error_message)
        """
        try:
            ydl_opts = {
                "writesubtitles": True,
                "subtitleslangs": ["en"],
                "skip_download": True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(video_url, download=False)

            subtitles = info.get("subtitles", {}).get("en", [])
            if not subtitles:
                return (
                    None,
                    "No subtitles are available for this video. Please try another video.",
                )

            subtitle_url = subtitles[0]["url"]
            response = requests.get(subtitle_url)
            if response.status_code != 200:
                return (
                    None,
                    f"Failed to retrieve subtitles (HTTP {response.status_code}). Please try again later.",
                )

            subtitle_data = response.json()
            text_lines = []
            for event in subtitle_data.get("events", []):
                for segment in event.get("segs", []):
                    text = segment.get("utf8", "").strip()
                    if text:
                        text_lines.append(text)

            subtitle_text = " ".join(text_lines)
            subtitle_text = re.sub(
                r"Transcriber:.*?\n|Reviewer:.*?\n", "", subtitle_text
            )
            subtitle_text = re.sub(r"\n", " ", subtitle_text)
            subtitle_text = re.sub(r"\s{2,}", " ", subtitle_text)

            return (
                subtitle_text.strip(),
                None,
            )  # Return subtitle text and no error message

        except yt_dlp.DownloadError as e:
            return (
                None,
                f"An error occurred while extracting the video info: {str(e)}. Please check the video URL and try again.",
            )

        except requests.exceptions.RequestException as e:
            return (
                None,
                f"An issue occurred while retrieving the subtitle file: {str(e)}. Please check your internet connection and try again.",
            )

        except KeyError as e:
            return (
                None,
                f"Unexpected response format while processing subtitles. It seems like some data is missing or corrupted: {str(e)}.",
            )

        except Exception as e:
            return (
                None,
                f"An unexpected error occurred: {str(e)}. Please try again later or contact support.",
            )

    @staticmethod
    def create_subtitles_file(subtitle_text: str, video_url: str) -> tuple[str, str]:
        """
        Create a temporary subtitle file and return its path

        Args:
            subtitle_text: The subtitle text content
            video_url: Original video URL for naming

        Returns:
            tuple: (file_path, filename)
        """
        # Create a temporary file
        fd, path = tempfile.mkstemp(suffix=".txt")
        with os.fdopen(fd, "w") as tmp:
            tmp.write(subtitle_text)

        # Extract video ID or use a default name
        video_id = (
            video_url.split("v=")[-1].split("&")[0]
            if "v=" in video_url
            else "subtitles"
        )
        filename = f"{video_id}_subtitles.txt"

        return path, filename
