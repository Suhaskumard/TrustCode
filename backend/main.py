from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="TrustCode Academic Integrity API", version="0.1.0")


class IntegrityPolicy(BaseModel):
    name: str
    max_similarity: float = Field(ge=0.0, le=100.0)
    ai_strictness: float = Field(ge=0.0, le=1.0)
    originality_weight: float = Field(ge=0.0, le=1.0)
    citation_weight: float = Field(ge=0.0, le=1.0)
    novelty_weight: float = Field(ge=0.0, le=1.0)


class IntegritySignals(BaseModel):
    originality_score: float = Field(ge=0.0, le=100.0)
    citation_quality_score: float = Field(ge=0.0, le=100.0)
    logic_flow_score: float = Field(ge=0.0, le=100.0)
    novelty_score: float = Field(ge=0.0, le=100.0)
    writing_quality_score: float = Field(ge=0.0, le=100.0)
    ai_overuse_risk: float = Field(ge=0.0, le=100.0)
    idea_similarity_risk: float = Field(ge=0.0, le=100.0)


class EvidenceItem(BaseModel):
    section: str
    reason: str
    confidence: float = Field(ge=0.0, le=1.0)
    source: Optional[str] = None


class IntegrityScoreResponse(BaseModel):
    integrity_index: float
    verdict: str
    evidence: List[EvidenceItem]


POLICIES: List[IntegrityPolicy] = []


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/policies", response_model=IntegrityPolicy)
def create_policy(policy: IntegrityPolicy) -> IntegrityPolicy:
    POLICIES.append(policy)
    return policy


@app.get("/policies", response_model=List[IntegrityPolicy])
def list_policies() -> List[IntegrityPolicy]:
    return POLICIES


@app.post("/score", response_model=IntegrityScoreResponse)
def score_submission(signals: IntegritySignals) -> IntegrityScoreResponse:
    index = (
        0.25 * signals.originality_score
        + 0.15 * signals.citation_quality_score
        + 0.15 * signals.logic_flow_score
        + 0.15 * signals.novelty_score
        + 0.10 * signals.writing_quality_score
        - 0.10 * signals.ai_overuse_risk
        - 0.10 * signals.idea_similarity_risk
    )

    verdict = "pass" if index >= 60 else "review"
    evidence = [
        EvidenceItem(
            section="Overall",
            reason="Composite index derived from originality, citation quality, logic flow, novelty, and risk penalties.",
            confidence=0.86,
        ),
        EvidenceItem(
            section="AI Usage",
            reason="AI-overuse risk reduces the final index under institutional policy.",
            confidence=0.78,
            source="policy:default-weight-profile",
        ),
    ]

    return IntegrityScoreResponse(
        integrity_index=round(index, 2),
        verdict=verdict,
        evidence=evidence,
    )
