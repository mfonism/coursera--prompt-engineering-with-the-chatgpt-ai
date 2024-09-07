import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "python quiz. 5 questions."}],
    max_tokens=256,
)

breakpoint()

# print(response.choices[0].message.content)
