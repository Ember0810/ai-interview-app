import os
from openai import OpenAI


def generate_response(prompt: str) -> str | None:
    """
    使用 GPT 模型根據 prompt 生成文字回覆
    """

    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.responses.create(
            model="gpt-5-nano",
            input=prompt,
            store=True
        )

        return response.output_text
    except Exception as e:
        print(f"❌ generate_response 錯誤: {e}")
        return None
