import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
)

def call(text: str):
    resp = client.chat.completions.create(
        model=os.getenv("LLM_MODEL"),
        messages=[{"role": "user", "content": text}],
    )

    content = resp.choices[0].message.content
    usage = resp.usage
    return content, usage

def call_with_stream(text: str):
    stream = client.responses.create(
        model=os.getenv("LLM_MODEL"),
        input=[{"role": "user", "content": text}],
        stream = True
    )

    return stream