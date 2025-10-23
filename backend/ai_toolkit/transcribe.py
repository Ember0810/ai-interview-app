import os
from openai import OpenAI


def transcribe_audio(file_path: str, language: str = "zh") -> str | None:
    """
    將音訊檔轉成文字（使用 Whisper）
    """
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        with open(file_path, "rb") as audio:
            transcript = client.audio.transcriptions.create(
                model="gpt-4o-mini-transcribe",
                file=audio,
                language=language
            )
        return transcript.text
    except Exception as e:
        print(f"❌ transcribe_audio 錯誤: {e}")
        return None
