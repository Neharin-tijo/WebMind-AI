# test_retrieval.py

import faiss
import pickle

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("vectorstore/index.faiss")

with open("vectorstore/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

query = "What services does this company offer?"

query_embedding = model.encode([query])

distances, indices = index.search(query_embedding, 3)

for i in indices[0]:

    print("\n")
    print(chunks[i][:500])
    