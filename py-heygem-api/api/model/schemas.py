from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ModelBase(BaseModel):
    name: str
    video_path: Optional[str] = None
    audio_path: Optional[str] = None
    voice_id: Optional[str] = None

class ModelCreate(ModelBase):
    pass

class ModelUpdate(BaseModel):
    name: Optional[str] = None
    video_path: Optional[str] = None
    audio_path: Optional[str] = None
    voice_id: Optional[str] = None

class ModelOut(ModelBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
