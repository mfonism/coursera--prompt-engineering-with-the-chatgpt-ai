import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    {
        "role": "system",
        "content": "You are an expert Python instructor. Your task is to generate quizzes for Python programming with multiple-choice questions, providing options and answers.",
    },
    {
        "role": "user",
        "content": """Create a 5-question Python quiz with 4 multiple-choice options for each question. Include the correct answer at the end of each question. The quiz should cover basic to intermediate Python topics like data types, loops, functions, and error handling.

Example format:
1. Which of the following data types is immutable in Python?
a) List
b) Dictionary
c) Set
d) Tuple

Correct answer: d) Tuple""",
    },
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    max_tokens=1000,
)

breakpoint()

# print(response.choices[0].message.content)
