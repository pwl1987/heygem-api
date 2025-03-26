import os
from config import settings

def init_data_dirs():
    os.makedirs(settings.TTS_AUDIO_DIR, exist_ok=True)
    print(f"Initialized data directories at: {settings.TTS_AUDIO_DIR}")

if __name__ == "__main__":
    init_data_dirs()
