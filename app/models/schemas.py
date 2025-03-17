from pydantic import BaseModel


class TranslationRequest(BaseModel):
    text: str


class TranslationResponse(BaseModel):
    original: str
    translated: str


class VideoRequest(BaseModel):
    video_url: str


class ErrorResponse(BaseModel):
    error: str
