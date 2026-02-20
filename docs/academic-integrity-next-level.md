# Academic Integrity Platform – Level-3 Blueprint

## 1) Product goal

Build an enterprise-ready academic integrity system that moves beyond string matching and supports **idea-level authenticity**, **explainable decisioning**, and **institution-scale analytics**.

## 2) Core modules

| Layer | Responsibilities |
|---|---|
| AI Engine | embeddings, stylometry, argument mining, multilingual NLP |
| Integrity Engine | weighted scoring, policy evaluation, penalties, thresholds |
| Explainability | source snippets, confidence, rationale trace |
| Analytics | student, class, department, institution trend intelligence |
| Governance | policy authoring, audit logs, ethics + consent handling |
| Research | novelty analysis and anonymized dataset export |

## 3) Prioritized implementation roadmap

### Phase A: Trust foundation (Weeks 1–3)
- Policy-Driven Rules Engine
- Evidence-Backed Decision Reports
- Academic Integrity Index (first version)

### Phase B: Detection intelligence (Weeks 4–8)
- Concept-Level Plagiarism Detector
- AI-vs-Human Writing Probability
- Stylometric fingerprint + anomaly detection
- Contribution verification for team submissions

### Phase C: Research quality (Weeks 9–12)
- Argument & Logic Flow Analyzer
- Novelty Score against historical/internal/public sources
- Viva-support auto question generator
- Learning Outcome mapping (Bloom/CO/PO)

### Phase D: Enterprise scale (Weeks 13–16)
- Batch/college analytics dashboards
- Improvement timeline per student
- Multi-language support + cross-language similarity
- Secure dataset builder with ethics controls

## 4) Academic Integrity Index (proposed v1)

```text
IntegrityIndex =
(0.25 * OriginalityScore)
+ (0.15 * CitationQualityScore)
+ (0.15 * LogicFlowScore)
+ (0.15 * NoveltyScore)
+ (0.10 * WritingQualityScore)
- (0.10 * AIOveruseRisk)
- (0.10 * IdeaSimilarityRisk)
```

Policy engine can override weights by institution.

## 5) Data entities (minimal)

- StudentProfile
- Submission
- EvidenceItem
- IntegrityPolicy
- AnalysisResult
- ContributionSplit
- OutcomeMapping
- AuditEvent

## 6) Explainability contract

Every flagged result must include:
- evidence snippet
- matched source
- score/confidence
- model signal summary
- policy/rule that fired

This keeps outcomes auditable and defensible during viva/disciplinary reviews.

## 7) Research/IEEE readiness

- Anonymized dataset pipeline with consent metadata
- Experiment tracking for model versions
- Baseline comparison (classical plagiarism vs idea-level model)
- Fairness checks across language/background segments

## 8) Suggested KPIs

- False positive rate (<5% target)
- Manual review agreement (>85%)
- Policy override frequency
- Semester-over-semester integrity improvement
- Time saved in faculty review process
