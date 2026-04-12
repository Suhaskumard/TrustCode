from pydantic import BaseModel, HttpUrl
from typing import Optional, Dict, Any, List
from enum import Enum

class AnalysisType(str, Enum):
    SECURITY = "security"
    QUALITY = "quality"
    COMPLEXITY = "complexity"

class RepoAnalysisRequest(BaseModel):
    repo_url: HttpUrl

class Metric(BaseModel):
    name: str
    value: float
    max_value: float
    description: str

class TrustScore(BaseModel):
    overall: float  # 0-100
    factors: Dict[str, float]
    grade: str  # A-F

class AnalysisResponse(BaseModel):
    repo_name: str
    repo_url: str
    stars: int
    forks: int
    open_issues: int
    commits: int
    trust_score: TrustScore
    ai_insights: Dict[str, str]
    metrics: List[Metric]
    summary: str
    recommendations: List[str]

