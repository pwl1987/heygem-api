from fastapi import FastAPI
from config import settings

app = FastAPI(
    title="Heygem API",
    description="Python版Heygem API服务",
    version="1.0.0",
    openapi_url=f"{settings.API_PREFIX}/openapi.json"
)

@app.get("/")
async def root():
    return {"message": "Heygem API服务运行中"}

# 注册各模块路由
from api.model import router as model_router
from api.tts import router as tts_router
from api.tts.audio import router as tts_audio_router
from api.video import router as video_router
from api.video.output import router as video_output_router
from api.voice import router as voice_router
from api.voice.output import router as voice_output_router
from api.auth import router as auth_router
from api.logging import router as logging_router

app.include_router(model_router, prefix=settings.API_PREFIX)
app.include_router(tts_router, prefix=settings.API_PREFIX)
app.include_router(tts_audio_router)
app.include_router(video_router, prefix=settings.API_PREFIX)
app.include_router(video_output_router)
app.include_router(voice_router, prefix=settings.API_PREFIX)
app.include_router(voice_output_router)
app.include_router(auth_router, prefix=settings.API_PREFIX)
app.include_router(logging_router, prefix=settings.API_PREFIX)
