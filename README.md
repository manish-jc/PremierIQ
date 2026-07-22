# ⚽ PremierIQ

> **AI-Powered Premier League Analytics Platform using Hybrid RAG, FastAPI, React, Gemini AI and FAISS**

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?logo=react)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![Gemini](https://img.shields.io/badge/Google-Gemini_AI-4285F4?logo=google)
![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-orange)
![RAG](https://img.shields.io/badge/Hybrid-RAG-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Overview

PremierIQ is an AI-powered football analytics platform designed for the English Premier League.

Instead of manually searching through statistics and historical records, users can ask natural language questions and receive intelligent, data-driven responses.

The application combines traditional football analytics with **Hybrid Retrieval-Augmented Generation (Hybrid RAG)** to provide accurate and contextual answers while also supporting player analytics, club analytics, rankings, and comparisons.

---

# ✨ Features

### 🤖 AI Chat

- Ask football questions using natural language
- Hybrid RAG-powered responses
- Gemini AI integration
- Semantic search using FAISS

Example:

> Who is Harry Kane?

> Compare Mohamed Salah and Erling Haaland

> Top scorers in 2022

---

### 👤 Player Analytics

- Player profile
- Goals
- Assists
- Position
- Nationality
- Market Value
- Club Information

---

### 🏆 Club Analytics

- Club profile
- Squad information
- Season statistics
- Historical data

---

### 📊 Rankings

- Top Scorers
- Top Assists
- Goalkeeper Rankings

---

### ⚖️ Player Comparison

Compare two players based on:

- Goals
- Assists
- Matches Played
- Position
- Club
- Other statistics

---

### 🔍 Hybrid RAG Pipeline

PremierIQ combines:

- Semantic Search
- Football Analytics Database
- FAISS Vector Search
- Gemini AI

to generate intelligent football insights.

---

# 🏗 System Architecture

```
                    React Frontend
                           │
                           ▼
                    FastAPI Backend
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
 Player Analytics    Club Analytics      AI Chat
                                              │
                                              ▼
                                    Question Router
                                              │
                                     Entity Extraction
                                              │
                                     Context Builder
                                              │
                                     FAISS Retriever
                                              │
                                          Gemini AI
                                              │
                                   Football Knowledge Base
```

---

# 🛠 Tech Stack

## Frontend

- React
- React Router
- Axios
- Tailwind CSS
- Lucide React

## Backend

- Python
- FastAPI
- Uvicorn
- Pandas

## AI

- Google Gemini
- Hybrid RAG
- FAISS
- Sentence Transformers

## Data

- Premier League Dataset
- Football Statistics
- CSV Processing

---

# 📂 Project Structure

```
PremierIQ
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   └── services/
│
├── app/
│   ├── api/
│   ├── rag/
│   ├── analytics/
│   ├── services/
│   └── database/
│
├── data/
│
├── vector_store/
│
├── screenshots/
│
├── requirements.txt
└── README.md
```

---

# 📸 Screenshots

## 🏠 Home Page

```
screenshots/home.png
```

---

## 🤖 AI Chat

```
screenshots/chat.png
```

---

## 📊 Rankings

```
screenshots/rankings.png
```

---

## ⚖️ Player Comparison

```
screenshots/comparison.png
```

---

## 📖 FastAPI Swagger

```
screenshots/swagger.png
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/manish-jc/PremierIQ.git
```

```bash
cd PremierIQ
```

---

## Backend

```bash
python -m venv venv
```

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn app.api.main:app --reload
```

Backend

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

---

## Frontend

```bash
cd frontend
```

```bash
npm install
```

```bash
npm run dev
```

Frontend

```
http://localhost:5173
```

---

# 📡 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/chat` | AI Chat |
| `/player` | Player Profile |
| `/club` | Club Profile |
| `/rankings/top-scorers` | Top Scorers |
| `/rankings/top-assists` | Top Assists |
| `/rankings/goalkeepers` | Goalkeeper Rankings |
| `/comparisons/player` | Player Comparison |

---

# 💡 Future Enhancements

- Live Premier League Data
- Interactive Visualizations
- Player Recommendation Engine
- Conversation Memory
- Multi-League Support
- Match Prediction
- Transfer Analytics
- Team Performance Dashboard

---

# 🎓 Learning Outcomes

This project helped strengthen practical experience in:

- Retrieval-Augmented Generation (RAG)
- FastAPI Development
- React Frontend Development
- REST API Design
- Vector Databases
- FAISS Search
- LLM Integration
- Football Data Analytics
- Full Stack Development

---

# 👨‍💻 Author

**Manish J C**

GitHub: https://github.com/manish-jc

LinkedIn: https://linkedin.com/in/YOUR_PROFILE

---


If you found this project interesting, consider giving it a ⭐ on GitHub.
