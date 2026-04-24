# TrustCode Platform – Autonomous AI Analyst

## 📌 Project Overview
A production-ready web application that analyzes GitHub repositories using AI-powered analysis to generate **Trust Scores**, code quality insights, security risks, and comprehensive reports.


## 🎯 Features 
- 🔍 GitHub Repo Analysis via API
- 🤖 AI-powered code quality & security scanning
- 📊 Trust Score (0-100) with breakdown
- 🎨 Responsive dashboard (React + Tailwind)
- 🚀 FastAPI backend with modular services
- 🐳 Docker Compose for easy deployment
- 🔐 Secure (env vars, CORS, error handling)

## 🧩 Architecture
```
trustcode-platform/                           # Root: Full-stack GitHub Trust Analyzer
├── backend/                                 # 🐍 FastAPI Backend API (localhost:8000)
│   ├── Dockerfile                           # Backend Docker build
│   ├── requirements.txt                     # Python deps (fastapi, pydantic, httpx)
│   ├── main.py                              # FastAPI app entrypoint (/health, /analyze-repo)
│   ├── models/schemas.py                    # Pydantic models (RepoAnalysisResponse)
│   ├── utils/github_api.py                  # GitHub API client (fetch repo tree/files)
│   ├── services/ai_analyzer.py              # AI code scanning logic
│   └── services/trust_engine.py             # Trust Score calculation (0-100)
├── frontend/                                # ⚛️ React + Vite + Tailwind UI (localhost:3000)
│   ├── Dockerfile                           # Frontend Docker build
│   ├── package.json                         # NPM deps (react, vite, axios)
│   ├── vite.config.js                       # Vite bundler config
│   ├── tailwind.config.js                   # Tailwind CSS config
│   ├── postcss.config.js                    # PostCSS config
│   ├── index.html                           # HTML entrypoint
│   └── src/
│       ├── main.jsx                         # React root render
│       ├── App.jsx                          # Main dashboard component
│       ├── index.css                        # Global styles
│       └── api.js                           # API client (calls backend)
├── docker-compose.yml                       # 🐳 Orchestrates backend (8000) + frontend (3000) services
├── README.md                                # 📖 This documentation
├── TODO.md                                  # ✅ Implementation tasks complete
└── TODO_ARCH.md                             # 📋 Architecture update tracking
```

### 🐳 Docker Services
| Service | Port | Description |
|---------|------|-------------|
| backend | 8000 | FastAPI API (/docs, /analyze-repo) |
| frontend | 3000 | React app (Vite dev server) |

### 🔄 Data Flow
```
User (browser) → Frontend (React) → API Call → Backend (FastAPI)
                ↓
GitHub API (utils/github_api.py) → Repo Data → AI Analyzer + Trust Engine
                ↓
JSON Response → Frontend Dashboard (Trust Score gauge, insights)
```

## 🚀 Quick Start

1. **Clone & Setup**
```bash
git clone <repo>
cd trustcode-platform
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
# Add your GITHUB_TOKEN to backend/.env
```

2. **Run with Docker**
```bash
docker-compose up --build
```

## 📋 API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/analyze-repo/{repo_url}` | POST | Analyze repo (body: empty JSON) |

**Example**:
```bash
curl -X POST "http://localhost:8000/analyze-repo/https://github.com/fastapi/fastapi"
```

## 🛠️ Tech Stack
- **Backend**: FastAPI, Pydantic, httpx
- **Frontend**: React 18, Vite, Tailwind CSS
- **DevOps**: Docker Compose
- **AI**: Modular analyzer (LLM-ready)

## 📸 Screenshots
*(Placeholder - Add after running)*
- Dashboard with Trust Score gauge
- Repo metrics & AI insights
- Responsive mobile view

## 🔧 Development

**Backend**:
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

**Frontend**:
```bash
cd frontend
npm install
npm run dev
```

## 🌟 Future Improvements 
- Real LLM integration (OpenAI/Groq)
- Rate limiting & caching
- Repo file content analysis
- Export reports (PDF)





