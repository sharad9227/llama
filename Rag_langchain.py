

from sentence_transformers import SentenceTransformer, util
from loadcsv_1 import embedder,data
import numpy as np
import torch
def retrieve_info(query):
    query_embedding = embedder.encode(query)

    # Convert the list of embeddings to a single numpy array
    embeddings_list = data['embedding'].tolist()
    embeddings_array = np.array(embeddings_list)

    # Convert the numpy array to a PyTorch tensor
    embeddings_tensor = torch.from_numpy(embeddings_array)

    # Convert query embedding to tensor if not already
    query_embedding_tensor = torch.tensor(query_embedding)

    # Calculate cosine similarity scores
    scores = util.pytorch_cos_sim(query_embedding_tensor, embeddings_tensor)

    # Find the index of the highest similarity score
    top_index = scores.argmax().item()

    return data.iloc[top_index]
