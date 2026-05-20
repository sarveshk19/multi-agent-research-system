# Multi-Agent Research System

An AI-powered Multi-Agent Research System built using PydanticAI, Groq, and FastAPI.

## Features

- Research Agent
- Summarizer Agent
- Citation Generator
- Structured AI Outputs
- FastAPI Backend
- Groq LLM Integration
- Multi-Agent Architecture

---

# Tech Stack

- Python
- FastAPI
- PydanticAI
- Groq API
- Pydantic
- AsyncIO

---

# Project Structure

```bash
multi-agent-research-system/
│
├── agents/
│   ├── researcher.py
│   ├── summarizer.py
│   ├── citation.py
│   └── coordinator.py
│
├── models/
│   └── research_models.py
│
├── tools/
│
├── prompts/
├── tests/
│
├── .gitignore
├── .env
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-research-system.git
```

## Move into Project

```bash
cd multi-agent-research-system
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Setup Environment Variables

Create `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# Run Project

```bash
uvicorn main:app --reload
```

Server runs on:

```bash
http://127.0.0.1:8000
```

---

# API Endpoint

## Research Endpoint

```bash
GET /research?query=AI Agents
```

Example:

```bash
http://127.0.0.1:8000/research?query=Future%20of%20AI
```

---

# Example Response

```json
{
  "research": {
    "topic": "Future of AI",
    "findings": [
      {
        "title": "AI Agents",
        "summary": "AI agents are becoming autonomous systems...",
        "source": "Research Source"
      }
    ]
  },
  "summary": {
    "overview": "AI systems are rapidly evolving...",
    "key_points": [
      "Autonomous AI",
      "Multi-agent systems",
      "Agentic workflows"
    ]
  },
  "citations": {
    "citations": [
      "Source 1",
      "Source 2"
    ]
  }
}
```

---

# Future Improvements

- Tavily Web Search
- RAG Pipeline
- LangGraph Integration
- ChromaDB
- PDF Export
- React Frontend
- Docker Deployment
- Redis Memory
- Streaming Responses

---

# Author

Sarvesh Kombe
