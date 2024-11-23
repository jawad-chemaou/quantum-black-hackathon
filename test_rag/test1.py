import os
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": "mon nombre secret est 10",
        },
    ]
)
print(chat_response.choices[0].message.content)

chat_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": "Quel est mon nombre secret?",
        },
    ]
)

print(chat_response.choices[0].message.content)