# CI/CD Notes

- Main workflow lives at `.github/workflows/ci.yml`.
- Add deploy jobs for Render/AWS in a separate environment-specific workflow.
- Recommended enhancement: trust-based merge gate using a GitHub Check that reads `/api/commits/{id}` risk output.
