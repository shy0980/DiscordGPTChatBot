import openai

secret_key = "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"

openai.api_key = secret_key

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]

while True:
    message = input("User : ")
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
