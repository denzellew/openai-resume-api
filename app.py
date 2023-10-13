from dotenv import load_dotenv
load_dotenv()

from generate_prompts import generate_prompts
from openai_adapter import openai_chat


messages = generate_prompts("Google", "Software Engineer", "We are looking for a software engineer to join our team. You will be responsible for maintaining and improving our backend infrastructure.")
chat_response = openai_chat(messages)

print(chat_response)