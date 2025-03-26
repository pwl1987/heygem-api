from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os
from config import settings

router = APIRouter()

@router.get("/tts/audio/{file_id}.wav")
async def get_audio_file(file_id: str):
    file_path = os.path.join(settings.TTS_AUDIO_DIR, f"{file_id}.wav")
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="Audio file not found"
        )
    return FileResponse(
        file_path,
        media_type="audio/wav",
        filename=f"{file_id}.wav"
    )
