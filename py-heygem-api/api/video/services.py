from celery import Celery
from config import settings
from pydantic import BaseModel
from typing import Optional
import os
import subprocess
import shutil
from .schemas import VideoProcessResponse, VideoStatus

celery = Celery(
    'video_tasks',
    broker=settings.CELERY_BROKER,
    backend=settings.CELERY_BACKEND
)

@celery.task(bind=True)
def process_video(self, file_path: str, task_id: str):
    try:
        # 更新任务状态为处理中
        self.update_state(
            state=VideoStatus.PROCESSING,
            meta={
                "task_id": task_id,
                "status": VideoStatus.PROCESSING
            }
        )

        # 创建输出目录
        output_dir = os.path.join(settings.VIDEO_OUTPUT_DIR, task_id)
        os.makedirs(output_dir, exist_ok=True)

        # 输出文件路径
        output_path = os.path.join(output_dir, "processed.mp4")

        # 使用FFmpeg处理视频 (示例: 转码为H.264)
        cmd = [
            "ffmpeg",
            "-i", file_path,
            "-c:v", "libx264",
            "-preset", "fast",
            "-crf", "22",
            "-c:a", "aac",
            "-b:a", "128k",
            output_path
        ]
        subprocess.run(cmd, check=True)

        # 返回处理结果
        return VideoProcessResponse(
            task_id=task_id,
            status=VideoStatus.COMPLETED,
            output_url=f"/video/output/{task_id}/processed.mp4"
        ).dict()

    except Exception as e:
        return VideoProcessResponse(
            task_id=task_id,
            status=VideoStatus.FAILED,
            error=str(e)
        ).dict()
    finally:
        # 清理临时文件
        if os.path.exists(file_path):
            os.remove(file_path)
