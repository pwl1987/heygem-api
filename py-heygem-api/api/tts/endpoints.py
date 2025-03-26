from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from ..schemas import TTSRequest, TTSResponse
from ..services import text_to_speech
from database import get_db
from config import settings
from celery.result import AsyncResult
import uuid

router = APIRouter(prefix=settings.API_PREFIX)

@router.post("/tts", response_model=TTSResponse)
async def convert_text_to_speech(
    request: TTSRequest,
    db: AsyncSession = Depends(get_db)
):
    try:
        task_id = str(uuid.uuid4())
        task = text_to_speech.delay(
            text=request.text,
            voice_id=request.voice_id,
            task_id=task_id
        )
        return {
            "task_id": task_id,
            "status_url": f"{settings.API_PREFIX}/tts/status/{task_id}"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"TTS转换失败: {str(e)}"
        )

@router.get("/tts/status/{task_id}", response_model=TTSResponse)
async def get_tts_status(
    task_id: str,
    db: AsyncSession = Depends(get_db)
):
    task = AsyncResult(task_id)
    if not task.ready():
        return {
            "task_id": task_id,
            "status": "processing"
        }
    
    if task.failed():
        raise HTTPException(
            status_code=500,
            detail="TTS处理失败"
        )
    
    return task.get()
