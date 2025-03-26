from pydantic import BaseModel
from typing import Optional
from enum import Enum

class VoiceType(str, Enum):
    MALE = "male"
    FEMALE = "female"
    CHILD = "child"

class TTSRequest(BaseModel):
    text: str
    voice_id: VoiceType = VoiceType.FEMALE
    speed: Optional[float] = 1.0
    pitch: Optional[float] = 1.0
    volume: Optional[float] = 1.0

class TTSResponse(BaseModel):
    task_id: str
    status: str
    audio_url: Optional[str] = None
    error: Optional[str] = None

class TTSStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
