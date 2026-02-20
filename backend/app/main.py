from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse

from app.data import COMMITS, DEPENDENCY_GRAPH, RESEARCH_BASELINE
from app.risk_engine import score_commit
from app.schemas import CIInsight, Commit, CommitIngest, DashboardSummary, ResearchComparison

app = FastAPI(title="Trust Code Platform API", version="0.3.0")

MERGE_POLICY = {"block_threshold": 75.0, "review_threshold": 50.0}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/commits")
def list_commits() -> list[dict]:
    rows: list[dict] = []
    for commit in COMMITS:
        risk = score_commit(commit)
        rows.append(
            {
                "id": commit.id,
                "author": commit.author,
                "message": commit.message,
                "risk_score": risk.risk_score,
                "risk_level": risk.risk_level,
                "failure_probability": risk.failure_probability,
            }
        )
    return rows


@app.post("/api/webhooks/github/commit")
def ingest_commit(payload: CommitIngest) -> dict:
    exists = next((c for c in COMMITS if c.id == payload.id), None)
    if exists:
        raise HTTPException(status_code=409, detail="Commit ID already exists")

    commit = Commit(**payload.model_dump())
    COMMITS.insert(0, commit)
    risk = score_commit(commit)
    return {
        "status": "ingested",
        "commit_id": commit.id,
        "risk_level": risk.risk_level,
        "failure_probability": risk.failure_probability,
    }


@app.get("/api/commits/{commit_id}")
def commit_deep_dive(commit_id: str) -> dict:
    commit = next((c for c in COMMITS if c.id == commit_id), None)
    if not commit:
        raise HTTPException(status_code=404, detail="Commit not found")

    risk = score_commit(commit)
    return {
        "commit": commit.model_dump(),
        "risk": risk.model_dump(),
        "ownership": {
            "owner": commit.author,
            "impacted_services": commit.modules_impacted,
            "blast_radius": "high" if commit.modules_impacted >= 4 else "moderate",
            "dependency_links": DEPENDENCY_GRAPH["auth"] if "auth" in commit.message.lower() else DEPENDENCY_GRAPH["analytics"],
        },
        "ci": {
            "estimated_pipeline_time_min": 18 + commit.files_changed,
            "recommended_test_scope": "selective" if risk.risk_level != "high" else "full",
            "merge_gate": "blocked" if risk.risk_score >= MERGE_POLICY["block_threshold"] else "needs-review" if risk.risk_score >= MERGE_POLICY["review_threshold"] else "pass",
        },
    }


@app.get("/api/ownership/blast-radius/{commit_id}")
def blast_radius(commit_id: str) -> dict:
    commit = next((c for c in COMMITS if c.id == commit_id), None)
    if not commit:
        raise HTTPException(status_code=404, detail="Commit not found")

    affected = commit.modules_impacted
    chain = DEPENDENCY_GRAPH["checkout"] if affected > 3 else DEPENDENCY_GRAPH["analytics"]
    return {
        "commit_id": commit.id,
        "owner": commit.author,
        "modules_impacted": affected,
        "upstream_downstream_dependencies": chain,
        "blast_radius_score": min(affected * 18, 100),
    }


@app.get("/api/merge-gate/evaluate/{commit_id}")
def merge_gate(commit_id: str) -> dict:
    commit = next((c for c in COMMITS if c.id == commit_id), None)
    if not commit:
        raise HTTPException(status_code=404, detail="Commit not found")

    risk = score_commit(commit)
    if risk.risk_score >= MERGE_POLICY["block_threshold"]:
        decision = "blocked"
    elif risk.risk_score >= MERGE_POLICY["review_threshold"]:
        decision = "manual-review"
    else:
        decision = "approved"

    return {
        "commit_id": commit_id,
        "risk_score": risk.risk_score,
        "decision": decision,
        "policy": MERGE_POLICY,
        "auto_comment": f"Trust Gate: {decision}. Predicted failure probability is {int(risk.failure_probability * 100)}%.",
    }


@app.get("/api/merge-gate/policy")
def merge_policy() -> dict:
    return MERGE_POLICY


@app.put("/api/merge-gate/policy")
def update_merge_policy(block_threshold: float, review_threshold: float) -> dict:
    if block_threshold <= review_threshold:
        raise HTTPException(status_code=400, detail="block_threshold must be greater than review_threshold")
    MERGE_POLICY["block_threshold"] = block_threshold
    MERGE_POLICY["review_threshold"] = review_threshold
    return {"status": "updated", "policy": MERGE_POLICY}


@app.post("/api/predict/what-if")
def what_if(payload: CommitIngest) -> dict:
    simulated = Commit(**payload.model_dump())
    risk = score_commit(simulated)
    return {
        "risk": risk.model_dump(),
        "recommendation": "Split commit and add tests" if risk.risk_score > 70 else "Safe to proceed with selective tests",
    }


@app.get("/api/dashboard/summary", response_model=DashboardSummary)
def dashboard_summary() -> DashboardSummary:
    risks = [score_commit(c) for c in COMMITS]
    high_risk = len([r for r in risks if r.risk_level == "high"])
    trust_score = round(100 - (sum(r.risk_score for r in risks) / len(risks)) * 0.55)

    return DashboardSummary(
        trust_score=max(trust_score, 0),
        high_risk_commits=high_risk,
        avg_ci_time_min=16.4,
        selective_testing_savings_min=41.5,
    )


@app.get("/api/analytics/failure-trends")
def failure_trends() -> dict:
    risks = [score_commit(c) for c in COMMITS]
    return {
        "weekly_failure_rate": [0.22, 0.19, 0.14, 0.17, 0.11, 0.09],
        "hotspots": [
            {"module": "auth", "incidents": 8},
            {"module": "checkout", "incidents": 6},
            {"module": "analytics", "incidents": 3},
        ],
        "current_avg_predicted_failure": round(sum(r.failure_probability for r in risks) / len(risks), 2),
    }


@app.get("/api/ci/insights", response_model=CIInsight)
def ci_insights() -> CIInsight:
    return CIInsight(
        avg_pipeline_time_min=16.4,
        estimated_monthly_ci_cost_usd=241.8,
        selective_testing_time_saved_min=126.0,
        flaky_test_rate=0.07,
    )


@app.get("/api/trust-model")
def trust_model() -> dict:
    weights = {
        "blast_radius": 0.3,
        "test_coverage_delta": 0.25,
        "historical_failures": 0.27,
        "change_size": 0.18,
    }
    return {
        "model": "Weighted heuristic classifier v2",
        "weights": weights,
        "explainability": [
            "Each commit receives a score from 0-100.",
            "Score increases with larger blast radius and poor testing signals.",
            "Trust score is inversely derived from aggregate commit risk.",
            "Merge gate requires manual review when risk exceeds medium threshold.",
        ],
    }


@app.get("/api/research/comparison", response_model=ResearchComparison)
def research_comparison() -> ResearchComparison:
    return ResearchComparison(
        period="Semester 2026",
        avg_risk_before=RESEARCH_BASELINE["avg_risk_before"],
        avg_risk_after=RESEARCH_BASELINE["avg_risk_after"],
        trust_gain_percent=RESEARCH_BASELINE["trust_gain_percent"],
        deployment_failure_drop_percent=RESEARCH_BASELINE["deployment_failure_drop_percent"],
    )


@app.get("/api/reports/semester", response_class=PlainTextResponse)
def semester_report() -> str:
    rows = ["metric,value", "avg_risk_before,68.4", "avg_risk_after,44.2", "trust_gain_percent,23.1", "deployment_failure_drop_percent,31.6"]
    return "\n".join(rows)


@app.get("/api/roles/{role}")
def role_dashboard(role: str) -> dict:
    base = {
        "developer": {
            "focus": "Improve commit hygiene and test quality",
            "widgets": ["my-risk-trend", "xai-feedback", "suggested-actions"],
        },
        "manager": {
            "focus": "Delivery risk, team velocity, and CI efficiency",
            "widgets": ["team-risk-heatmap", "ci-cost", "mttr", "release-confidence"],
        },
        "admin": {
            "focus": "Governance, policy, and evaluation reporting",
            "widgets": ["policy-rules", "audit-log", "semester-report"],
        },
    }
    if role not in base:
        raise HTTPException(status_code=404, detail="Role not found")
    return base[role]
