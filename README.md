# RAG Career Assistant

An AI-powered career assistant that combines Retrieval-Augmented Generation (RAG), Large Language Models, semantic search, web search, and live job listings to provide resume-grounded career assistance.

## Overview

RAG Career Assistant allows users to interact with information contained in their resume while also accessing external job information.

The system combines:

* Resume document processing
* Semantic search using embeddings
* FAISS vector retrieval
* Groq-powered LLM responses
* Web search
* Live Indian job recommendations through the Adzuna Jobs API

The project demonstrates how RAG and tool-based AI systems can be combined to build a practical career-focused AI assistant.

## Key Features

### 1. Resume RAG

The system loads a PDF resume, splits the document into smaller chunks, converts the chunks into vector embeddings, and stores them in a FAISS vector store.

Users can then ask questions about their resume using semantic retrieval.

### 2. LLM-Powered Responses

The project uses a Groq-hosted LLM through LangChain to generate responses using retrieved resume information.

### 3. Semantic Search

Instead of relying only on keyword matching, the system uses embeddings to retrieve semantically relevant resume content.

### 4. Web Search

The assistant includes a web search tool for retrieving external information.

### 5. Live Job Recommendations

The project integrates the Adzuna Jobs API to search for job opportunities based on:

* Job title
* Minimum salary

For example:

```text
Data Analyst
Minimum salary: 40000
```

### 6. Tool-Based Architecture

The project demonstrates multiple tools working together:

```text
Resume Retrieval
       │
       ├── RAG / FAISS
       │
       ├── Web Search
       │
       └── Job Search API
              │
              ▼
          AI Assistant
```

## Architecture

```text
                 ┌─────────────────────┐
                 │      User Query      │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    AI Assistant     │
                 └──────────┬──────────┘
                            │
              ┌─────────────┼─────────────┐
              │             │             │
              ▼             ▼             ▼
        Resume RAG     Web Search    Job Search
              │             │             │
              ▼             ▼             ▼
            FAISS       DuckDuckGo    Adzuna API
              │
              ▼
        Resume Context
              │
              └─────────────┐
                            ▼
                    ┌───────────────┐
                    │   Groq LLM    │
                    └───────┬───────┘
                            │
                            ▼
                    Final AI Response
```

## RAG Pipeline

```text
PDF Resume
    │
    ▼
PyPDFLoader
    │
    ▼
Text Extraction
    │
    ▼
RecursiveCharacterTextSplitter
    │
    ▼
Document Chunks
    │
    ▼
Ollama Embeddings
    │
    ▼
FAISS Vector Store
    │
    ▼
Semantic Retrieval
    │
    ▼
Relevant Resume Context
    │
    ▼
Groq LLM
    │
    ▼
Generated Response
```

## Tech Stack

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Core programming language       |
| LangChain     | LLM and RAG orchestration       |
| Groq          | LLM inference                   |
| FAISS         | Vector similarity search        |
| Ollama        | Local embedding generation      |
| PyPDF         | PDF document processing         |
| DuckDuckGo    | Web search                      |
| Adzuna API    | Job listing search              |
| python-dotenv | Environment variable management |
| Requests      | API communication               |

## Project Structure

```text
rag-career-assistant/
│
├── app.py
├── rag.py
├── tools.py
├── llm_config.py
│
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── LICENSE
│
├── data/
│   └── sample_resume.pdf
│
├── assets/
│   └── architecture.png
│
└── screenshots/
    └── demo.png
```

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd rag-career-assistant
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-20b

ADZUNA_APP_ID=your_adzuna_app_id
ADZUNA_APP_KEY=your_adzuna_app_key
```

Never commit the `.env` file to GitHub.

A safe configuration template is provided in:

```text
.env.example
```

## Ollama Setup

This project uses Ollama for local embeddings.

Install Ollama and make sure the Ollama service is running.

Then download the embedding model used by the project:

```bash
ollama pull all-minilm
```

Verify that Ollama is running before starting the RAG pipeline.

## Running the Project

Run the main application:

```bash
python app.py
```

Or run the RAG pipeline directly:

```bash
python rag.py
```

The system will process the resume and allow you to submit queries.

## Example Queries

### Resume Questions

```text
What are my technical skills?
```

```text
What projects are mentioned in my resume?
```

```text
What Python experience do I have?
```

```text
Summarize my data analytics experience.
```

### Job Search

```text
Find Data Analyst jobs.
```

```text
Find Data Analyst jobs with a minimum salary of 40000.
```

## Example Workflow

```text
User
 │
 ▼
Question
 │
 ▼
Tool Selection
 │
 ├──────────────► Resume RAG
 │
 ├──────────────► Web Search
 │
 └──────────────► Job API
 │
 ▼
Retrieved Information
 │
 ▼
Groq LLM
 │
 ▼
Context-Aware Response
```

## Security

API credentials are intentionally excluded from this repository.

The project uses environment variables:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
```

The `.gitignore` file prevents `.env` from being committed.

## Important Security Rule

Never commit:

```text
.env
```

Never place API keys directly inside Python files.

Do not share API keys in screenshots, README files, notebooks, or GitHub issues.

## Limitations

* Job availability depends on the external job API.
* Search results depend on the configured external services.
* Resume responses are limited by the information available in the uploaded document.
* Local embedding generation requires Ollama to be installed and running.
* API credentials are required for external services.

## Future Improvements

* Add a conversational memory layer
* Add a modern web interface
* Add multi-format resume support
* Add resume scoring against job descriptions
* Add skill-gap analysis
* Add job ranking based on resume similarity
* Add personalized learning recommendations
* Add persistent vector database storage
* Add evaluation metrics for RAG retrieval quality
* Add automated RAG evaluation using relevant benchmarks

## Learning Outcomes

This project demonstrates practical experience with:

* Retrieval-Augmented Generation
* Vector embeddings
* Semantic search
* Vector databases
* LLM integration
* LangChain
* Tool calling
* API integration
* Document processing
* Environment variable management
* AI agent architecture

## Author

**Ingale Dipak Mohan**

B.Sc. Data Science Student

Interested in:

* Data Analytics
* Data Science
* Artificial Intelligence
* Machine Learning
* Generative AI
* Agentic AI

This project is licensed under the MIT License.

