import json
import faiss
import pickle
import os

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def chunk_text(text, chunk_size=500):
    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


def load_pages():
    with open("data/pages.json", "r", encoding="utf-8") as f:
        return json.load(f)


def create_embeddings():
    pages = load_pages()

    all_chunks = []
    metadata = []

    for url, content in pages.items():

        chunks = chunk_text(content)

        for chunk in chunks:
            all_chunks.append(chunk)
            metadata.append(url)

    embeddings = model.encode(all_chunks)

    return embeddings, all_chunks, metadata


def build_faiss():

    os.makedirs("vectorstore", exist_ok=True)

    embeddings, chunks, metadata = create_embeddings()

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    faiss.write_index(index, "vectorstore/index.faiss")

    with open("vectorstore/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    with open("vectorstore/metadata.pkl", "wb") as f:
        pickle.dump(metadata, f)

    print("FAISS Index Saved")


if __name__ == "__main__":
    build_faiss()
    