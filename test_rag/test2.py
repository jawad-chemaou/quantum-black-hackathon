from mistralai import Mistral
import numpy as np
import os
from getpass import getpass
import time
import pandas as pd 


api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-small"

client = Mistral(api_key=api_key)


import csv

csv_file = 'amazon.csv'

df = pd.read_csv(csv_file)
print(df.columns)

# df = df.head(1000)


columns_to_embed = ['product_name', 'category', 'about_product', 'review_title', 'review_content']


def get_text_embedding(input):
    time.sleep(0.25)
    embeddings_batch_response = client.embeddings.create(
          model="mistral-embed",
          inputs=input
      )
    return embeddings_batch_response.data[0].embedding

# create and store embeddings for each column in the dataframe

for column in columns_to_embed[:1]:
    print(f'Embedding column {column}')
    df[column + '_embedding'] = df[column].apply(get_text_embedding)


print(df.head())

# save the dataframe to a new csv file
df.to_csv('amazon_embeddings.csv', index=True)

#text_embeddings = np.array([get_text_embedding(chunk) for chunk in chunks])

#print(text_embeddings)
"""
import faiss

d = text_embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(text_embeddings)


question = "What type of cable do  you sell?"
question_embeddings = np.array([get_text_embedding(question)])

"""




