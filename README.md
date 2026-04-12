# 🚀 TrustCode Platform – Autonomous AI Analyst

## 📌 Overview

**TrustCode Platform** is a full-stack AI-powered system that evaluates GitHub repositories and generates a **Trust Score (0–100)** based on code quality, security, and project reliability.

It helps developers, recruiters, and organizations quickly assess whether a repository is **safe, maintainable, and production-ready**.

## ✨ Key Highlights

* 🔍 Automated GitHub repository analysis
* 🤖 AI-driven code quality & security insights
* 📊 Trust Score with detailed breakdown
* ⚡ FastAPI backend with scalable architecture
* 🎨 Modern React dashboard (Vite + Tailwind)
* 🐳 Fully containerized with Docker Compose
* 🔐 Secure configuration using environment variables

## 🎯 Features

### 🔎 Repository Analysis

* Fetch repository metadata via GitHub API
* Analyze structure, files, and signals

### 🤖 AI Code Intelligence

* Code quality heuristics
* Security issue detection
* Extendable LLM integration (future-ready)

### 📊 Trust Score Engine

* Score range: **0–100**
* Factors:

  * Code quality
  * Security risks
  * Project structure
  * Maintainability

### 🖥️ Interactive Dashboard

* Clean UI built with React + Tailwind
* Displays:

  * Trust Score
  * Insights
  * Risk indicators

## 🧩 Architecture

```
trustcode-platform/
│
├── backend/                     # FastAPI Backend (Port 8000)
│   ├── main.py                  # API entrypoint
│   ├── models/                  # Pydantic schemas
│   ├── services/                # AI + Trust logic
│   └── utils/                   # GitHub API client
│
├── frontend/                    # React App (Port 3000)
│   ├── src/
│   │   ├── App.jsx              # Main UI
│   │   └── api.js               # API integration
│
├── docker-compose.yml           # Multi-container setup
└── README.md
```

## 🔄 System Workflow

```
User Input (Repo URL)
        ↓
Frontend (React UI)
        ↓
API Request → FastAPI Backend
        ↓
GitHub API → Fetch Repo Data
        ↓
AI Analyzer + Trust Engine
        ↓
Trust Score + Insights (JSON)
        ↓
Frontend Dashboard Visualization
```

## 🐳 Docker Services

| Service  | Port | Description             |
| -------- | ---- | ----------------------- |
| backend  | 8000 | FastAPI API             |
| frontend | 3000 | React (Vite dev server) |

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Suhaskumard/TrustCode.git
cd trustcode-platform
```

### 2️⃣ Setup Environment Variables

```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
```

👉 Add your GitHub token:

```
GITHUB_TOKEN=your_token_here
```

### 3️⃣ Run with Docker

```bash
docker-compose up --build
```

### 4️⃣ Access the Application

* 🌐 Frontend → [http://localhost:3000](http://localhost:3000)
* 📘 API Docs → [http://localhost:8000/docs](http://localhost:8000/docs)
* ❤️ Health Check → [http://localhost:8000/health](http://localhost:8000/health)

## 📡 API Reference

### 🔹 Health Check

```http
GET /health
```

### 🔹 Analyze Repository

```http
POST /analyze-repo/{repo_url}
```

### Example:

```bash
curl -X POST "http://localhost:8000/analyze-repo/https://github.com/fastapi/fastapi"
```

## 🛠️ Tech Stack

### Backend

* FastAPI
* Pydantic
* httpx

### Frontend

* React 18
* Vite
* Tailwind CSS

### DevOps

* Docker
* Docker Compose

### AI Layer

* Modular Analyzer (LLM-ready architecture)

## 🔐 Security Practices

* Environment-based configuration (`.env`)
* API input validation using Pydantic
* CORS handling
* No hardcoded secrets

## ⚙️ Development Setup

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## 📈 Future Enhancements

* 🔗 LLM Integration (OpenAI / Groq)
* 📦 Repository deep file analysis
* ⚡ Caching & rate limiting
* 📄 Export reports (PDF / JSON)
* 🔐 Authentication system
* 📊 Historical analytics dashboard

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

## 🧠 Use Cases

* 🧑‍💻 Developers → Evaluate dependencies
* 🧑‍💼 Recruiters → Assess candidate projects
* 🏢 Companies → Validate open-source usage
* 🎓 Students → Improve code quality

## 📜 License

This project is licensed under the MIT License.

## ❤️ Acknowledgements

* GitHub API
* Open-source ecosystem
* AI research community

## 👨‍💻 Author

**Suhas Kumar**

## 🌟 Final Note

TrustCode is built with a vision to make **code trust measurable**.

> “Not all repositories are equal — TrustCode helps you prove it.”

