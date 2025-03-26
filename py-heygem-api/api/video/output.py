from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os
from config import settings

router = APIRouter()

@router.get("/video/output/{task_id}/{filename}")
async def get_video_output(task_id: str, filename: str):
    file_path = os.path.join(settings.VIDEO_OUTPUT_DIR, task_id, filename)
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="视频文件不存在"
        )
    return FileResponse(
        file_path,
        media_type="video/mp4",
        filename=filename
    )
