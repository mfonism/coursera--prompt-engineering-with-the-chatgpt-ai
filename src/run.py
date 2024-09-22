import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    {
        "role": "system",
        "content": "You are an expert Python instructor. Generate Python quizzes with multiple-choice questions, including options and correct answers.",
    },
    {
        "role": "user",
        "content": """Create a 5-question Python quiz with 4 multiple-choice options per question, covering basic to intermediate topics like data types, loops, functions, and error handling. Ensure each question has a difficulty level of 7/10. Include the correct answer at the end of each question, randomly positioned among the options.

Example format:
1. Which of the following data types is immutable in Python?
a) List
b) Dictionary
c) Set
d) Tuple

Correct answer: d) Tuple""",
    },
]

def get_completions(messages):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=1000,
    )

    return response.choices[0].message.content
