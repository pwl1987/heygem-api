from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os
from config import settings

router = APIRouter()

@router.get("/voice/output/{task_id}/{filename}")
async def get_voice_output(task_id: str, filename: str):
    file_path = os.path.join(settings.VOICE_OUTPUT_DIR, task_id, filename)
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="语音文件不存在"
        )
    return FileResponse(
        file_path,
        media_type="audio/wav",
        filename=filename
    )
