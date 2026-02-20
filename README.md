# Developer Trust & Code Reliability Platform

A full-stack platform for commit risk analysis, trust scoring, explainable AI, CI insights, and governance-oriented merge control.

## Monorepo Structure

```text
frontend/      # Next.js 14 dashboard UI
backend/       # FastAPI service with analytics endpoints
ai-engine/     # Risk scoring logic and model stubs
ci/            # CI/CD support assets
database/      # SQL schema
cloud/         # Cloud integration notes
docs/          # Architecture, roadmap, API catalog
.github/       # GitHub Actions workflows
```

## Advanced Features Implemented

- Predictive risk scoring before CI starts
- What-if commit simulation endpoint for pre-merge planning
- Explainable AI reason panel for risk changes
- Code ownership + blast radius endpoint and UI
- Trust-based merge gate evaluation + policy endpoints and UI
- Role-based dashboards (Developer, Manager, Admin)
- Research comparison endpoint (before vs after Trust Loop)
- Semester CSV report export endpoint
- CI time/cost optimization insights
- Simulated webhook ingestion endpoint for new commits

## Quick Start

### Backend

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Set `NEXT_PUBLIC_API_BASE_URL=http://localhost:8000` in `frontend/.env.local`.
