# System Architecture

## Components

1. **Frontend (Next.js + Tailwind)**
   - Renders dashboards and analytics views.
   - Pulls data from FastAPI endpoints.

2. **Backend (FastAPI)**
   - Serves commit analytics, trust score, and role-oriented summaries.
   - Exposes explainability data and CI optimization metrics.

3. **AI Engine (Python package)**
   - Provides deterministic risk scoring now, swappable with ML models later.
   - Supplies reason codes used in Explainable AI panel.

4. **Data Layer (PostgreSQL-ready schema)**
   - Commit, author, pipeline, and score history tables.

5. **CI/CD (GitHub Actions)**
   - Runs backend syntax check and frontend lint/build.

## Data Flow

`GitHub webhook/commit payload -> backend risk engine -> trust score/explanations -> frontend dashboards`

## Research Angle

- Persist historical scores per commit and compare pre/post trust-loop interventions.
- Analyze distribution shifts for failure probability and MTTR indicators.
