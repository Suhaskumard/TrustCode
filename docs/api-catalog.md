# API Catalog (Advanced)

## Core
- `GET /health`
- `GET /api/commits`
- `GET /api/commits/{commit_id}`

## Advanced Risk + Governance
- `POST /api/webhooks/github/commit`
- `POST /api/predict/what-if`
- `GET /api/ownership/blast-radius/{commit_id}`
- `GET /api/merge-gate/evaluate/{commit_id}`
- `GET /api/merge-gate/policy`
- `PUT /api/merge-gate/policy?block_threshold=80&review_threshold=55`

## Analytics + Research
- `GET /api/dashboard/summary`
- `GET /api/analytics/failure-trends`
- `GET /api/ci/insights`
- `GET /api/trust-model`
- `GET /api/research/comparison`
- `GET /api/reports/semester`
- `GET /api/roles/{role}`
