from pydantic import BaseModel, Field


class Commit(BaseModel):
    id: str
    author: str
    message: str
    files_changed: int
    modules_impacted: int
    tests_touched: bool
    historical_failure_rate: float


class CommitIngest(BaseModel):
    id: str
    author: str
    message: str
    files_changed: int = Field(ge=1)
    modules_impacted: int = Field(ge=1)
    tests_touched: bool
    historical_failure_rate: float = Field(ge=0.0, le=1.0)


class RiskResponse(BaseModel):
    commit_id: str
    risk_score: float
    risk_level: str
    failure_probability: float
    explanation: list[str]


class DashboardSummary(BaseModel):
    trust_score: int
    high_risk_commits: int
    avg_ci_time_min: float
    selective_testing_savings_min: float


class CIInsight(BaseModel):
    avg_pipeline_time_min: float
    estimated_monthly_ci_cost_usd: float
    selective_testing_time_saved_min: float
    flaky_test_rate: float


class ResearchComparison(BaseModel):
    period: str
    avg_risk_before: float
    avg_risk_after: float
    trust_gain_percent: float
    deployment_failure_drop_percent: float
