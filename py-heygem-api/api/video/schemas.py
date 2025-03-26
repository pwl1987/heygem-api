from pydantic import BaseModel
from typing import Optional
from enum import Enum

class VideoFormat(str, Enum):
    MP4 = "mp4"
    AVI = "avi"
    MOV = "mov"
    FLV = "flv"
    MKV = "mkv"

class VideoProcessRequest(BaseModel):
    format: VideoFormat = VideoFormat.MP4
    resolution: Optional[str] = "1080p"
    bitrate: Optional[int] = 4000
    fps: Optional[int] = 30

class VideoProcessResponse(BaseModel):
    task_id: str
    status: str
    output_url: Optional[str] = None
    error: Optional[str] = None

class VideoStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
