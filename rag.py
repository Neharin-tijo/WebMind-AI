import os
import faiss
import pickle
from google import genai

from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("vectorstore/index.faiss")

# Load chunks
with open("vectorstore/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

# Load metadata
with open("vectorstore/metadata.pkl", "rb") as f:
    metadata = pickle.load(f)


def retrieve_context(query, top_k=5):
    """
    Retrieve the most relevant chunks from FAISS.
    """

    query_embedding = embedding_model.encode([query])

    distances, indices = index.search(query_embedding, top_k)

    retrieved_chunks = []
    sources = []

    for idx in indices[0]:
        if idx >= 0:
            retrieved_chunks.append(chunks[idx])
            sources.append(metadata[idx])

    return retrieved_chunks, list(set(sources))


def answer_question(query):
    """
    Generate an answer using retrieved context.
    """

    retrieved_chunks, sources = retrieve_context(query)

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
Answer ONLY using the website content below.

If the answer is not available in the content, say:

"I could not find that information on the website."

Website Content:
{context}

Question:
{query}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text, sources


# Test locally
if __name__ == "__main__":

    question = input("Ask a question: ")

    answer, sources = answer_question(question)

    print("\nAnswer:\n")
    print(answer)

    print("\nSources:")
    for source in sources:
        print(source)
        