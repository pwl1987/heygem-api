from celery import Celery
from config import settings
from pydantic import BaseModel
from typing import Optional
import os
import subprocess
import shutil
from .schemas import VoiceProcessResponse, VoiceStatus

celery = Celery(
    'voice_tasks',
    broker=settings.CELERY_BROKER,
    backend=settings.CELERY_BACKEND
)

@celery.task(bind=True)
def process_voice(self, file_path: str, task_id: str):
    try:
        # 更新任务状态为处理中
        self.update_state(
            state=VoiceStatus.PROCESSING,
            meta={
                "task_id": task_id,
                "status": VoiceStatus.PROCESSING
            }
        )

        # 创建输出目录
        output_dir = os.path.join(settings.VOICE_OUTPUT_DIR, task_id)
        os.makedirs(output_dir, exist_ok=True)

        # 输出文件路径
        output_path = os.path.join(output_dir, "processed.wav")

        # 使用FFmpeg处理语音 (示例: 降噪和标准化)
        cmd = [
            "ffmpeg",
            "-i", file_path,
            "-af", "highpass=f=200,lowpass=f=3000,volume=2.0",
            "-ar", "16000",
            "-ac", "1",
            output_path
        ]
        subprocess.run(cmd, check=True)

        # 返回处理结果
        return VoiceProcessResponse(
            task_id=task_id,
            status=VoiceStatus.COMPLETED,
            output_url=f"/voice/output/{task_id}/processed.wav"
        ).dict()

    except Exception as e:
        return VoiceProcessResponse(
            task_id=task_id,
            status=VoiceStatus.FAILED,
            error=str(e)
        ).dict()
    finally:
        # 清理临时文件
        if os.path.exists(file_path):
            os.remove(file_path)
