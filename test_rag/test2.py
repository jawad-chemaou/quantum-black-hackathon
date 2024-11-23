from mistralai import Mistral
import requests
import numpy as np
import faiss
import os
from getpass import getpass
import time

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-small"

client = Mistral(api_key=api_key)


import csv

csv_file = 'amazon.csv'
string_data = ''


with open(csv_file, mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)  # Lecture du fichier CSV
    for row in reader:
        # Convertir chaque ligne en chaîne, en utilisant un séparateur spécifique (par exemple, une virgule)
        string_data += ','.join(row) + '\n'  # Séparateur par une virgule, vous pouvez changer cela si nécessaire


string_data = string_data  # limiter la taille de la chaîne à 1 million de caractères
chunk_size = 2048
chunks = [string_data[i:i + chunk_size] for i in range(0, len(string_data), chunk_size)]
print(len(chunks))

def get_text_embedding(input):
    time.sleep(0.1)
    embeddings_batch_response = client.embeddings.create(
          model="mistral-embed",
          inputs=input
      )
    return embeddings_batch_response.data[0].embedding
text_embeddings = np.array([get_text_embedding(chunk) for chunk in chunks])

import faiss

d = text_embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(text_embeddings)


question = "What type of cable do  you sell?"
question_embeddings = np.array([get_text_embedding(question)])


D, I = index.search(question_embeddings, k=2) # distance, index
retrieved_chunk = [chunks[i] for i in I.tolist()[0]]


prompt = f"""
Context information is below.
---------------------
{retrieved_chunk}
---------------------
Given the context information and not prior knowledge, answer the query.
Query: {question}
Answer:
"""


def run_mistral(user_message, model="mistral-large-latest"):
    messages = [
        {
            "role": "user", "content": user_message
        }
    ]
    chat_response = client.chat.complete(
        model=model,
        messages=messages
    )
    return (chat_response.choices[0].message.content)

print(run_mistral(prompt))