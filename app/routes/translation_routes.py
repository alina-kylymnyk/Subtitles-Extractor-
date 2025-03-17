from fastapi import APIRouter, Depends
from app.models.schemas import TranslationRequest, TranslationResponse
from app.services.translation_service import TranslationService

router = APIRouter()


def get_translation_service():
    return TranslationService()


@router.post("/translate/", response_model=TranslationResponse)
async def translate_api(
    request: TranslationRequest,
    translation_service: TranslationService = Depends(get_translation_service),
):
    return translation_service.translate_to_ukrainian(request.text)
