import pandas as pd
from sentence_transformers import SentenceTransformer, util
# Load the CSV data
data = pd.read_csv('./common_medicines_for_symptoms.csv')
# Load the model for sentence embedding
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# Precompute embeddings for the data
data['embedding'] = data.apply(lambda row: embedder.encode(f"{row['Symptom']} {row['Health Issue']}"), axis=1)