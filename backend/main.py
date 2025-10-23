import os
from pathlib import Path
from dotenv import load_dotenv
from ai_toolkit import generate_response, transcribe_audio

load_dotenv(".env.dev")


BASE_DIR = Path(__file__).resolve().parents[1]  # 從 backend/main.py 回到 project/


def audio_transcription():
    audio_path = BASE_DIR / "backend" / "assets" / "audio.m4a"
    records = transcribe_audio(str(audio_path))
    return records


def text_analysis(input_text: str) -> str | None:
    prompt = f"""
    你是一位人資顧問，負責分析面試者的自我介紹內容，請根據以下文字判斷他的情緒與語氣傾向：

    【任務要求】
    1. 請根據文字內容推測這位面試者的語氣與情緒，例如：自信、謙虛、焦慮、正向、冷靜、緊張、樂觀等。
    2. 請說明你判斷的依據（例如詞彙、語氣、結構）。
    3. 最後請給出一段總結，用一句話概述他的整體情緒印象。

    【自我介紹內容】
    「{input_text}」

    請用繁體中文回答。
    """
    response = generate_response(prompt)
    return response


def main():

    intro_text = """
    大家好，我叫 Leo，喜歡學習新技術，也很樂於挑戰不同的專案。
    我知道自己還有很多不足，但我會努力補足，希望能在工作中持續成長。
    我認為團隊合作很重要，願意和同事們互相學習、互相支持，
    一起完成目標。謝謝大家給我這個機會，希望能成為團隊的一員！
    """
    print("Ans:", text_analysis(intro_text))


if __name__ == "__main__":
    main()
