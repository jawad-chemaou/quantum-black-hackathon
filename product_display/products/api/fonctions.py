import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords
import nltk
from mistralai import Mistral



from nltk.stem import WordNetLemmatizer
from sentence_transformers import SentenceTransformer
import os

api_key = os.environ["MISTRAL_API_KEY"]


client = Mistral(api_key=api_key)

# Charger les embeddings et les métadonnées
data = pd.read_csv('C://Users//artem//OneDrive//Documents//Elias//X3//hackathon//quantum-black-hackathon//chat_bot_mvp//text_embeddings.csv')  # Assumez que le fichier contient 'product_id', 'embedding'
# Si les embeddings sont des chaînes de nombres séparés par des espaces
embeddings = np.array(
    data['embedding']
    .apply(eval)  # Utiliser `eval` pour interpréter directement la liste encodée comme chaîne
    .tolist()  # Transformer la colonne en une liste de listes
)

product_strings = data['text'].values
from sklearn.metrics.pairwise import cosine_similarity

def find_nearest_neighbors(question_embedding, top_k=5):
    # Calculer la similarité cosinus
    similarities = cosine_similarity([question_embedding], embeddings)[0]
    # Trouver les indices des k produits les plus proches
    nearest_indices = np.argsort(similarities)[::-1][:top_k]
    # Retourner les IDs des produits correspondants
    return product_strings[nearest_indices], similarities[nearest_indices]



def get_embedding(input):

    embeddings_batch_response = client.embeddings.create(
          model="mistral-embed",
          inputs=input
      )
    return embeddings_batch_response.data[0].embedding


def generate_chunks(question):
    k = 30
    # Calcul de l'embedding de la question
    question_embedding = np.array([get_embedding(preprocess_text(question))]).reshape(1, -1)
    print('Taille question_embedding:', question_embedding.shape)
    print('Taille premier embedding:', embeddings[0].shape)
    
    # Calcul des similarités cosinus
    similarities = cosine_similarity(question_embedding, embeddings).flatten()
    
    # Tri par similarité décroissante et suppression des doublons
    idx_sorted_similarities = np.argsort(-similarities)[:k]
    unique_indices = np.unique(idx_sorted_similarities)
    
    print("Indices uniques triés par similarité:", unique_indices)
    
    # Récupération des chunks
    retrieved_chunks = [product_strings[i] for i in unique_indices]
    return retrieved_chunks


def preprocess_text(text):
    # Lowercasing
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    return text