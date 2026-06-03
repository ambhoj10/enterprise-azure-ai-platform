# Enterprise Azure AI Platform Architecture

## Overview

Enterprise Azure AI Platform is a cloud-native AI knowledge assistant built using Azure OpenAI, Azure AI Search, Azure Blob Storage, and FastAPI.

The platform enables enterprise document ingestion, indexing, retrieval, and Retrieval-Augmented Generation (RAG) workflows to provide grounded AI responses based on organizational knowledge.

---

## High-Level Architecture

```text
                    User
                      │
                      ▼

                 FastAPI API

      ┌─────────────┼─────────────┐
      │             │             │
      ▼             ▼             ▼

 Azure OpenAI   Azure AI Search   Azure Storage

      │             │             │
      │             │             │
      └─────────────┼─────────────┘
                    │
                    ▼

            Enterprise Documents
             TXT / PDF Files
```

---

## Request Flow

### Document Upload Flow

1. User uploads TXT or PDF document.
2. FastAPI receives the file.
3. DocumentParser extracts text.
4. Azure Blob Storage stores the original file.
5. Azure AI Search indexes extracted content.
6. Document becomes available for search and retrieval.

---

### Question Answering Flow

1. User submits a question.
2. FastAPI calls Azure AI Search.
3. Top relevant documents are retrieved.
4. Context is assembled from retrieved documents.
5. Context is sent to Azure OpenAI GPT-4o-mini.
6. AI generates a grounded response.
7. Response is returned with source citations.

---

## Core Components

### FastAPI

Responsibilities:

* REST API endpoints
* Request processing
* Service orchestration
* Health monitoring

---

### Azure OpenAI

Model:

* GPT-4o-mini

Responsibilities:

* Context-aware response generation
* Enterprise knowledge assistant
* Retrieval-Augmented Generation (RAG)

---

### Azure AI Search

Responsibilities:

* Document indexing
* Full-text search
* Retrieval of relevant knowledge
* Searchable content storage

---

### Azure Blob Storage

Responsibilities:

* Original document storage
* TXT file storage
* PDF file storage
* Long-term retention

---

### Document Parser

Supported Formats:

* TXT
* PDF

Responsibilities:

* Text extraction
* Document normalization
* Search ingestion preparation

---

## Security Design

Configuration Management:

* Environment Variables
* API Keys
* Azure Service Authentication

Sensitive Information:

* Stored in .env
* Excluded from Git via .gitignore

---

## Current Capabilities

* Azure OpenAI Integration
* Azure AI Search Integration
* Azure Blob Storage Integration
* TXT Document Ingestion
* PDF Document Ingestion
* RAG Knowledge Assistant
* Source Citations
* Health Monitoring

---

## Future Enhancements

### AI

* Vector Search
* Semantic Search
* Hybrid Search
* Multi-Agent Architecture
* Model Context Protocol (MCP)

### Platform

* GitHub Actions CI/CD
* Azure Container Apps
* Terraform Deployment Automation
* Azure Monitor Dashboards
* Application Insights Telemetry

---

## Version

Enterprise Azure AI Platform v1.0

Week 12 Capstone Project

