from app.schemas import Commit

COMMITS: list[Commit] = [
    Commit(
        id="cmt-101",
        author="Ayesha",
        message="Refactor auth middleware and token parser",
        files_changed=11,
        modules_impacted=4,
        tests_touched=False,
        historical_failure_rate=0.42,
    ),
    Commit(
        id="cmt-102",
        author="Rahul",
        message="Fix flaky checkout flow assertions",
        files_changed=3,
        modules_impacted=1,
        tests_touched=True,
        historical_failure_rate=0.18,
    ),
    Commit(
        id="cmt-103",
        author="Mei",
        message="Add caching for analytics endpoint",
        files_changed=7,
        modules_impacted=3,
        tests_touched=True,
        historical_failure_rate=0.27,
    ),
]

DEPENDENCY_GRAPH = {
    "auth": ["api-gateway", "session", "billing"],
    "checkout": ["cart", "payments", "inventory", "pricing"],
    "analytics": ["warehouse", "dashboard"],
}

RESEARCH_BASELINE = {
    "avg_risk_before": 68.4,
    "avg_risk_after": 44.2,
    "trust_gain_percent": 23.1,
    "deployment_failure_drop_percent": 31.6,
}
