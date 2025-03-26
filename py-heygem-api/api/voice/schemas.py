from pydantic import BaseModel
from typing import Optional
from enum import Enum

class VoiceProcessRequest(BaseModel):
    sample_rate: int = 16000
    channels: int = 1
    format: str = "wav"
    noise_reduction: bool = True
    volume_normalization: bool = True

class VoiceProcessResponse(BaseModel):
    task_id: str
    status: str
    output_url: Optional[str] = None
    error: Optional[str] = None

class VoiceStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
