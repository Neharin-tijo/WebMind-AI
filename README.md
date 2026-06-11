# 🌐 WebMind-AI

WebMind-AI is a Retrieval-Augmented Generation (RAG) based website chatbot that can ingest a website URL, recursively crawl pages, build a vector database from the extracted content, and answer user questions using AI.

## Features

* Website URL ingestion
* Recursive web crawling
* HTML content extraction
* Text chunking and preprocessing
* Vector embedding generation using Sentence Transformers
* Semantic search using FAISS
* AI-powered question answering with Google Gemini
* Source URL references
* Streamlit-based user interface

---

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
Sentence Transformer
    │
    ▼
FAISS Vector Database
    │
    ▼
Retriever
    │
    ▼
Gemini LLM
    │
    ▼
Answer + Sources
```

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI & RAG

* Google Gemini API
* Sentence Transformers

### Vector Database

* FAISS

### Web Scraping

* BeautifulSoup
* Requests

### Data Processing

* Pickle
* NumPy

---

## Project Structure

```text
WebMind-AI/
│
├── app.py
├── crawler.py
├── rag.py
├── embeddings.py
├── build_vectorstore.py
├── test_retrieval.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── pages.json
│
└── vectorstore/
    ├── index.faiss
    ├── index.pkl
    └── metadata.pkl
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Neharin-tijo/WebMind-AI.git
cd WebMind-AI
```

### Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
```

---

## Running the Project

Start the Streamlit application:

```bash
streamlit run app.py
```

---

## Usage

1. Enter a website URL.
2. Crawl the website.
3. Generate embeddings and build the vector database.
4. Ask questions about the website.
5. Receive answers along with source URLs.

---

## Example

### Input URL

```text
https://docs.streamlit.io
```

### Question

```text
What is Streamlit?
```

### Output

```text
Streamlit is an open-source Python framework for data scientists and AI/ML engineers to deliver dynamic data apps with only a few lines of code.
```

---

## Future Enhancements

* Multi-website support
* Automatic vector database rebuilding
* Chat history
* PDF and document ingestion
* Hybrid search
* Citation support

---

## Author

**Neharin Tijo**

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

* Google Gemini
* Sentence Transformers
* FAISS
* BeautifulSoup
* Streamlit
