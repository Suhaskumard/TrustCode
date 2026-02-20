# TrustCode Platform 🚀

TrustCode is an **Academic Integrity & Research Authenticity Platform** that helps faculty, students, and administrators evaluate originality, argument quality, AI overuse risk, and research novelty with explainable evidence.

## What is new (Next-Level Scope)

This repository now includes a practical implementation roadmap for the advanced Level-3 capabilities:

- Concept-level plagiarism detection (idea theft)
- Argument & logic-flow scoring
- AI-vs-human probability analysis
- Student stylometric fingerprinting
- Group contribution verification
- Research novelty scoring
- Viva support question generation
- Learning outcome mapping (CO/PO/Bloom)
- Batch/college analytics dashboards
- Policy-driven integrity rules
- Student improvement timeline
- Evidence-backed decision reports
- Secure dataset builder for research
- Multi-language support
- Composite Academic Integrity Index

## Top 10 must-build first

1. Policy-Driven Integrity Rules Engine
2. Evidence-Backed Decision Reports
3. Concept-Level Plagiarism Detector
4. AI vs Human Writing Probability
5. Stylometric Fingerprint + Drift Detection
6. Novelty Score Engine
7. Contribution Verification for Group Projects
8. Learning Outcome Mapping
9. Batch/College Analytics
10. Academic Integrity Index

Why this order:
- Delivers governance and trust early.
- Reduces false-positive risk by requiring explainability.
- Builds reusable scoring infrastructure before advanced UX layers.

## Initial API scaffold

A lightweight FastAPI scaffold is included at `backend/main.py` with:

- health endpoint
- policy registration endpoint
- integrity index scoring endpoint
- explainable evidence payload in the response

Run locally:

```bash
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload --port 8000
```

## Documentation

Detailed architecture, data model, phased rollout, and IEEE-friendly research framing:

- `docs/academic-integrity-next-level.md`
