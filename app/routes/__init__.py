from fastapi import APIRouter
from .subtitle_routes import router as subtitle_router
from .translation_routes import router as translation_router

router = APIRouter()

router.include_router(subtitle_router)
router.include_router(translation_router)
