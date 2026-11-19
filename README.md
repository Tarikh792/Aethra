# 💎 Aethra
### Intelligent Document Research Assistant

**Turn PDFs into interactive knowledge with Retrieval-Augmented Generation (RAG).**

Aethra is an AI-powered document assistant built with Python, Streamlit, Sentence Transformers, and Groq. It allows users to upload text-based PDF documents, ask natural-language questions, and receive context-grounded answers with source chunk references.

Unlike traditional keyword search, Aethra uses semantic embeddings to retrieve document passages based on meaning.

## ✨ Features

- **PDF Upload:** Upload and process text-based PDF documents.
- **Semantic Search:** Find relevant information using vector embeddings and cosine similarity.
- **AI-Powered Question Answering:** Generate document-grounded responses using Groq-hosted LLM inference.
- **Source References:** Display relevant document chunk identifiers.
- **Interactive Chat:** Ask questions through a Streamlit chat interface.
- **Conversation Display:** Maintain chat messages during the current session.
- **Document Caching:** Avoid unnecessary repeated PDF processing.
- **Premium Dark UI:** Responsive, midnight-blue interface with a document workspace.
- **Missing-Information Handling:** Instruct the language model to acknowledge when the retrieved context does not contain an answer.

## 🧠 How Aethra Works

Aethra implements a custom RAG pipeline without relying on a high-level orchestration framework.

```text
PDF Upload
    |
    v
Text Extraction (PyPDF)
    |
    v
Text Chunking
    |
    v
Vector Embeddings (Sentence Transformers)
    |
    v
Semantic Retrieval (Cosine Similarity)
    |
    v
Relevant Document Context
    |
    v
Groq Language Model
    |
    v
Grounded Answer + Source Chunk References
```

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Web Framework | Streamlit |
| PDF Processing | PyPDF |
| Embedding Model | all-MiniLM-L6-v2 |
| Vector Operations | NumPy |
| Similarity Search | Cosine Similarity |
| LLM Inference | Groq API |
| Language Model | OpenAI GPT-OSS 20B |

## 📁 Project Structure

```text
Aethra/
├── app.py
├── pdf_reader.py
├── chunker.py
├── embeddings.py
├── retriever.py
├── rag.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Module Responsibilities

- `app.py` — Streamlit interface, PDF uploads, chat history and document caching.
- `pdf_reader.py` — Extracts readable text from PDFs.
- `chunker.py` — Splits extracted text into overlapping chunks.
- `embeddings.py` — Converts text chunks into numerical vectors.
- `retriever.py` — Retrieves relevant chunks using cosine similarity.
- `rag.py` — Combines retrieved context with Groq language model inference.

## 🚀 Getting Started

### Prerequisites

- Python 3.11
- A Groq API key

### 1. Clone the Repository

```bash
git clone https://github.com/Tarikh792/Aethra.git
cd Aethra
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment.

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the API Key

Create a `.streamlit/secrets.toml` file:

```toml
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
```

Never commit API keys or secrets to version control.

### 5. Run the Application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, normally `http://localhost:8501`.

## 💬 Example Questions

After uploading a PDF, try asking:

- What is the main objective of this document?
- Summarize the key findings.
- Explain the methodology in simple language.
- What are the most important concepts discussed?
- Is there information about a specific topic?

Aethra retrieves relevant passages before generating its response.

## ⚠️ Current Limitations

Aethra is a Version 1 application with the following limitations:

- Scanned or image-only PDFs require OCR, which is not currently implemented.
- Source references identify text chunks, not verified PDF page numbers.
- Responses may occasionally be incomplete or inaccurate.
- Previous chat messages are displayed but are not passed to the language model for follow-up context.
- Semantic retrieval is performed in memory using NumPy rather than a dedicated vector database.
- Large documents may require additional memory and processing time.

## 🗺️ Future Improvements

- Page-level source citations
- Sentence-aware chunking
- Multi-document RAG
- Conversational follow-up support
- Retrieval evaluation and quality testing
- OCR support for scanned PDFs
- Improved retrieval ranking

## 👨‍💻 Author

**Syed Ali Tarikh**

AI Engineering & Generative AI Applications

GitHub: [@Tarikh792](https://github.com/Tarikh792)

## 🎬 Project Demo

[▶ Watch Aethra Demo Video](./Aethra%20Portfolio%20Demo.mp4)

---

Built to explore practical AI engineering through a custom Retrieval-Augmented Generation pipeline.
