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

The quiz should be challenging and not overly complex, and should be engaging for beginners to test their Python knowledge. Make sure to include a variety of question types and topics to keep the quiz interesting and informative. the options should be relevant and not too obvious, and the correct answer should be clear and concise. The correct answer should be randomly positioned among the options.

Each question should have a difficulty level of 7 on a scale of 1 to 10, with 10 being the most difficult.

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
