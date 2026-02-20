# Cloud Deployment Blueprint

## AWS Baseline
- Frontend: deploy Next.js on Vercel or ECS/Fargate.
- Backend: deploy FastAPI via ECS/EC2.
- Storage: S3 bucket for CI artifacts (videos, reports).
- Database: RDS PostgreSQL.

## Observability
- CloudWatch metrics for API latency and error rates.
- Alarm when risk evaluation endpoint p95 exceeds threshold.
