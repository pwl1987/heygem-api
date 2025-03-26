from fastapi import APIRouter
from .endpoints import voice

router = APIRouter(tags=["语音处理服务"])
router.include_router(voice.router, prefix="/voice")
