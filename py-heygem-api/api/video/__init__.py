from fastapi import APIRouter
from .endpoints import video

router = APIRouter(tags=["视频处理服务"])
router.include_router(video.router, prefix="/video")
