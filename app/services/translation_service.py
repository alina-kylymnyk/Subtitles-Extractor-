from fastapi import HTTPException
from googletrans import Translator


class TranslationService:
    def __init__(self):
        self.translator = Translator()

    def translate_to_ukrainian(self, text: str) -> dict:
        """
        Translate text from English to Ukrainian

        Args:
            text: Text to translate

        Returns:
            dict: Dictionary with original and translated text
        """
        try:
            if not text.strip():
                raise HTTPException(
                    status_code=400, detail="Input text cannot be empty."
                )

            translation = self.translator.translate(text, src="en", dest="uk")

            if not translation or not translation.text:
                raise HTTPException(status_code=500, detail="Translation failed.")

            return {"original": text, "translated": translation.text}

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error translating text: {e}")
