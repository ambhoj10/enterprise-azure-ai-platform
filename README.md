# Enterprise Azure AI Platform

## Overview

Enterprise Azure AI Platform is a cloud-native AI knowledge assistant built using Azure OpenAI, Azure AI Search, Azure Blob Storage, and FastAPI.

The platform supports document ingestion, indexing, retrieval, and Retrieval-Augmented Generation (RAG) workflows to provide AI-powered answers grounded in enterprise knowledge sources.

---

## Architecture

```text
                        User
                          │
                          ▼

                      FastAPI

          ┌─────────────┼─────────────┐
          │             │             │
          ▼             ▼             ▼

    Azure OpenAI   Azure AI Search   Blob Storage

          │             │             │
          └─────────────┼─────────────┘
                        │
                        ▼

                Enterprise Documents

                TXT / PDF Knowledge Base
```

---

## Key Features

### AI Capabilities

* Azure OpenAI GPT-4o-mini integration
* Retrieval-Augmented Generation (RAG)
* Context-aware AI responses
* Source citations
* Hallucination reduction through prompt grounding

### Search Capabilities

* Azure AI Search integration
* Full-text document search
* Top-K retrieval strategy
* Searchable document indexing

### Document Processing

* TXT document ingestion
* PDF document ingestion
* Automatic text extraction
* Search index population

### Platform Capabilities

* FastAPI REST APIs
* Health monitoring endpoint
* Modular service architecture
* Environment-based configuration

---

## Technology Stack

### Backend

* Python
* FastAPI

### Azure Services

* Azure OpenAI
* Azure AI Search
* Azure Blob Storage
* Azure Monitor
* Application Insights
* Log Analytics Workspace

### AI Components

* GPT-4o-mini
* Retrieval-Augmented Generation (RAG)

### Document Processing

* PyPDF
* Azure Search SDK

---

## Project Structure

```text
enterprise-azure-ai-platform
│
├── api
│   └── routes.py
│
├── app
│   ├── config.py
│   └── main.py
│
├── models
│   └── chat.py
│
├── services
│   ├── storage_service.py
│   ├── search_service.py
│   ├── openai_service.py
│   └── document_parser.py
│
├── observability
│   └── telemetry.py
│
├── docs
│   ├── architecture.md
│   └── screenshots
│
├── infrastructure
│   ├── scripts
│   └── terraform
│
├── requirements.txt
└── README.md
```

---

## API Endpoints

### Platform

```http
GET /
```

Returns platform status.

```http
GET /health
```

Returns health status.

---

### Document Management

```http
POST /upload
```

Upload document to Azure Blob Storage.

```http
POST /search/index
```

Create Azure AI Search index.

```http
POST /search/document
```

Index TXT and PDF documents into Azure AI Search.

---

### AI Assistant

```http
POST /chat
```

Ask questions against indexed enterprise documents.

Example:

```json
{
  "question": "What is Generative AI?"
}
```

Response:

```json
{
  "question": "What is Generative AI?",
  "answer": "Generative AI is ...",
  "sources": [
    "GEN-AI_for_beginners_to_pro.pdf"
  ]
}
```

---

## Azure Resources

### Azure OpenAI

* GPT-4o-mini Deployment

### Azure AI Search

* documents-index

### Azure Storage Account

* documents container

### Monitoring

* Application Insights
* Log Analytics Workspace

---

## Environment Variables

Create a `.env` file:

```env
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_DEPLOYMENT=

AZURE_SEARCH_ENDPOINT=
AZURE_SEARCH_API_KEY=
AZURE_SEARCH_INDEX=

AZURE_STORAGE_CONNECTION_STRING=
AZURE_STORAGE_CONTAINER=

APPLICATIONINSIGHTS_CONNECTION_STRING=
```

---

## Installation

Clone repository:

```bash
git clone <repository-url>
cd enterprise-azure-ai-platform
```

Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start application:

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Completed Capabilities

* Azure OpenAI Integration
* Azure AI Search Integration
* Azure Blob Storage Integration
* RAG Workflow
* Source Citations
* TXT Ingestion
* PDF Ingestion
* FastAPI APIs
* Enterprise Knowledge Assistant

---

## Future Enhancements

* Azure Monitor Dashboards
* Application Insights Telemetry
* Vector Search
* Hybrid Search
* Semantic Ranking
* Multi-Agent Architecture
* Model Context Protocol (MCP)
* GitHub Actions CI/CD
* Azure Container Apps Deployment

---

## Author

Ambhoj Kumar

Cloud & AI Platform Engineer
