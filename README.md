<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# RAG API with FastAPI

A Retrieval-Augmented Generation (RAG) API built with FastAPI that leverages ChromaDB for efficient knowledge retrieval and Ollama for local LLM inference.

**Project Link:** [View Project](http://learn.nextwork.org/projects/ai-devops-api)

**Author:** Jeanlee Barreto

---

## Overview

This project implements a RAG system that combines document embeddings with a large language model to provide accurate, context-aware responses. Documents are embedded and stored in ChromaDB, and queries are answered by retrieving relevant context and passing it to a local LLM.

## Features

- **Document Embedding**: Convert text documents into semantic embeddings using ChromaDB
- **Semantic Search**: Retrieve relevant documents based on query similarity
- **Local LLM Integration**: Use Ollama to run language models locally (TinyLLaMA)
- **RESTful API**: FastAPI endpoints for querying and adding knowledge
- **Persistent Storage**: Embeddings stored in ChromaDB with persistent database

## Architecture

```
┌─────────────┐
│   Client    │
└──────┬──────┘
       │
       ▼
┌──────────────────────────────────┐
│        FastAPI Server            │
│  ┌────────────────────────────┐  │
│  │ POST /query                │  │
│  │ POST /add                  │  │
│  └────────────────────────────┘  │
└──────────┬───────────────────────┘
           │
      ┌────┴────┐
      ▼         ▼
   ┌─────┐  ┌──────────────┐
   │Ollama│  │ChromaDB      │
   │ LLM │  │Embeddings DB │
   └─────┘  └──────────────┘
```

## Prerequisites

- Python 3.13
- [Ollama](https://ollama.ai) installed with TinyLLaMA model
- [UV](https://docs.astral.sh/uv/) package manager

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd nextwork-rag-api
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Setup embeddings (optional)**
   ```bash
   uv run ./embed.py
   ```
   This will process `k8s.txt` and create embeddings in the `./db` directory.

## Usage

### Start the API Server

```bash
uv run uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`

### API Endpoints

#### 1. Query Endpoint
Query the knowledge base with context-aware responses.

- **Endpoint**: `POST /query`
- **Parameter**: `q` (string) - Your question
- **Example**:
  ```bash
  curl -X POST "http://localhost:8000/query?q=What%20is%20Kubernetes%20manifest?" \
    -H "accept: application/json"
  ```
- **Response**:
  ```json
  {
    "answer": "Kubernetes manifests are YAML files that..."
  }
  ```

#### 2. Add Knowledge Endpoint
Dynamically add new content to the knowledge base.

- **Endpoint**: `POST /add`
- **Body**: Raw text content to add
- **Example**:
  ```bash
  curl -X POST "http://localhost:8000/add" \
    -H "Content-Type: text/plain" \
    -d '{
        "text": "Your knowledge base content here"
    }'
  ```
- **Response**:
  ```json
  {
    "status": "success",
    "message": "Content added to knowledge base",
    "id": "uuid-string"
  }
  ```

## Key Files

- **app.py**: Main FastAPI application
  - `/query` - Retrieves relevant documents and generates answers
  - `/add` - Adds new documents to the knowledge base

- **embed.py**: Embedding script
  - Reads documents from `k8s.txt`
  - Creates embeddings using ChromaDB
  - Stores embeddings in `./db` directory

- **k8s.txt**: Sample knowledge base content
  - Contains Kubernetes-related information used for initial embeddings

## Dependencies

- **chromadb** (>=1.4.1): Vector database for embeddings
- **fastapi** (>=0.128.5): Web framework for building APIs
- **ollama** (>=0.6.1): Python client for Ollama LLM
- **uvicorn** (>=0.40.0): ASGI web server

## Environment

- **Python**: 3.13
- **OS**: Windows/Mac/Linux (tested on Windows)
- **Database**: ChromaDB (local file-based storage)

## Notes

- Embeddings are created using ChromaDB's default embedding model (all-MiniLM-L6-v2)
- The LLM model (TinyLLaMA) must be available in Ollama before running queries
- The `db/` directory is created automatically on first run
- All embeddings are stored persistently in the `./db` directory
