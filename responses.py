import random
import openai
from decouple import config
api_key = config('API_GPT')

openai.api_key = api_key

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]


def handle_response(message) -> str:

    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})

    return reply
