import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    API_PREFIX: str = "/api/v1"
    DB_URL: str = "mysql+aiomysql://user:pass@localhost:3306/heygem"
    REDIS_URL: str = "redis://localhost:6379/0"
    CELERY_BROKER: str = "redis://localhost:6379/1"
    CELERY_BACKEND: str = "redis://localhost:6379/2"
    TTS_AUDIO_DIR: str = "data/tts_audio"
    VIDEO_TEMP_DIR: str = "data/video_temp"
    VIDEO_OUTPUT_DIR: str = "data/video_output"
    VOICE_TEMP_DIR: str = "data/voice_temp"
    VOICE_OUTPUT_DIR: str = "data/voice_output"
    SECRET_KEY: str = "your-secret-key-here"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        env_file = ".env"

settings = Settings()
