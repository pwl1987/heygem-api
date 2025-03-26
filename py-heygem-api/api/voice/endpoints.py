from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas import VoiceProcessRequest, VoiceProcessResponse
from ..services import process_voice
from database import get_db
from config import settings
from celery.result import AsyncResult
import uuid
import os

router = APIRouter(prefix=settings.API_PREFIX)

@router.post("/voice/process", response_model=VoiceProcessResponse)
async def process_voice_file(
    file: UploadFile,
    db: AsyncSession = Depends(get_db)
):
    try:
        # 生成唯一任务ID
        task_id = str(uuid.uuid4())
        
        # 保存上传文件到临时目录
        temp_dir = os.path.join(settings.VOICE_TEMP_DIR, task_id)
        os.makedirs(temp_dir, exist_ok=True)
        
        file_path = os.path.join(temp_dir, file.filename)
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())
        
        # 启动异步处理任务
        task = process_voice.delay(
            file_path=file_path,
            task_id=task_id
        )
        
        return {
            "task_id": task_id,
            "status_url": f"{settings.API_PREFIX}/voice/status/{task_id}"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"语音处理失败: {str(e)}"
        )

@router.get("/voice/status/{task_id}", response_model=VoiceProcessResponse)
async def get_voice_status(
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
            detail="语音处理失败"
        )
    
    return task.get()
