from fastapi import APIRouter
from .endpoints import tts

router = APIRouter(tags=["TTS服务"])
router.include_router(tts.router, prefix="/tts")
