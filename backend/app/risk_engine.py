from app.schemas import Commit, RiskResponse


def classify_risk(score: float) -> str:
    if score >= 75:
        return "high"
    if score >= 45:
        return "medium"
    return "low"


def score_commit(commit: Commit) -> RiskResponse:
    score = 0.0
    reasons: list[str] = []

    score += min(commit.files_changed * 2.2, 30)
    if commit.files_changed > 8:
        reasons.append("Large change set increases integration risk.")

    score += min(commit.modules_impacted * 4.5, 25)
    if commit.modules_impacted > 3:
        reasons.append("Blast radius spans multiple modules.")

    if not commit.tests_touched:
        score += 18
        reasons.append("No tests were updated alongside code changes.")

    score += commit.historical_failure_rate * 27
    if commit.historical_failure_rate > 0.4:
        reasons.append("Author/repository history shows elevated CI failures.")

    failure_probability = min(round(score / 100, 2), 0.95)
    risk_score = round(min(score, 100), 1)

    if not reasons:
        reasons.append("Change is small with healthy historical reliability.")

    return RiskResponse(
        commit_id=commit.id,
        risk_score=risk_score,
        risk_level=classify_risk(risk_score),
        failure_probability=failure_probability,
        explanation=reasons,
    )
