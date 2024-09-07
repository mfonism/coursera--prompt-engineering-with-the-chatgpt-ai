import os

from dotenv import load_dotenv

load_dotenv()

# Make sure to have a .env file in the root of the project
# it should contain the following line:
# FOO='It works, baby!'
print(os.getenv("FOO"))
