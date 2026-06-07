# WebMind-AI

WebMind-AI is an AI-powered website chatbot that can ingest a website URL, recursively crawl relevant pages, and answer user questions using Retrieval-Augmented Generation (RAG). The system extracts, processes, indexes, and retrieves website content to provide accurate, context-aware responses.

## Features

- Website URL ingestion
- Recursive crawling of linked pages
- Content extraction from HTML pages
- Text chunking and preprocessing
- Vector embeddings generation
- Semantic search using vector database
- Retrieval-Augmented Generation (RAG)
- Natural language question answering
- Fast and scalable architecture
- Support for structured and unstructured web content

## Architecture

```text
User URL
    │
    ▼
Web Crawler
    │
    ▼
Content Extraction
    │
    ▼
Text Chunking
    │
    ▼
Embedding Model
    │
    ▼
Vector Database
    │
    ▼
Retriever
    │
    ▼
LLM (RAG Pipeline)
    │
    ▼
Chatbot Response
```

## Tech Stack

### Frontend
- React.js / Next.js
- Tailwind CSS

### Backend
- Python
- FastAPI

### AI & RAG
- LangChain
- OpenAI / Gemini API
- Sentence Transformers

### Vector Database
- FAISS
- ChromaDB

### Web Scraping
- BeautifulSoup
- Requests
- Selenium (optional)

## Project Structure

```text
WebMind-AI/
│
├── frontend/
│   ├── src/
│   └── public/
│
├── backend/
│   ├── crawler/
│   ├── rag/
│   ├── api/
│   └── utils/
│
├── data/
│
├── vector_store/
│
├── requirements.txt
│
├── .env
│
└── README.md
```

## Installation

### Clone Repository

```bash
git clone https://github.com/Neharin-tijo/WebMind-AI.git
cd WebMind-AI
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
GEMINI_API_KEY=your_api_key
```

## Running the Project

### Backend

```bash
uvicorn main:app --reload
```

### Frontend

```bash
npm install
npm run dev
```

## Usage

1. Enter a website URL.
2. WebMind-AI crawls the website.
3. Content is extracted and indexed.
4. Ask questions about the website.
5. Receive context-aware answers generated through RAG.

### Example

Input URL:

```text
https://example.com
```

Question:

```text
What services does this company provide?
```

Output:

```text
The company provides web development, cloud consulting, and AI solutions.
```

## Future Enhancements

- Multi-website knowledge base
- PDF and document ingestion
- Real-time website updates
- Citation support
- Authentication and user management
- Conversation history
- Hybrid search (keyword + semantic)

## Contributors

- Neharin Tijo

## License

This project is licensed under the MIT License.

## Acknowledgements

- LangChain
- OpenAI
- Google Gemini
- ChromaDB
- FAISS
- FastAPI
