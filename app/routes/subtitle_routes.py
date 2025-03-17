from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
import os

from app.services.subtitle_service import SubtitleService

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.post("/process_video/")
async def process_video(request: Request, video_url: str = Form(...)):
    subtitle_text, error_message = SubtitleService.extract_subtitles(video_url)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "subtitle_text": subtitle_text,
            "error_message": error_message,
            "video_url": video_url,  # Keep the URL for the download form
        },
    )


@router.post("/download_subtitles/")
async def download_subtitles(video_url: str = Form(...)):
    subtitle_text, error_message = SubtitleService.extract_subtitles(video_url)

    if error_message:
        raise HTTPException(status_code=400, detail=error_message)

    # Create a temporary file for download
    path, filename = SubtitleService.create_subtitles_file(subtitle_text, video_url)

    # Return the file as a download
    return FileResponse(
        path,
        media_type="text/plain",
        filename=filename,
        background=lambda: os.remove(path),  # Delete the temporary file after download
    )
