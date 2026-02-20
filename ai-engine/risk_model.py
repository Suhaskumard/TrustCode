"""Standalone risk model stub for experimentation."""

from dataclasses import dataclass


@dataclass
class Features:
    files_changed: int
    modules_impacted: int
    tests_touched: bool
    historical_failure_rate: float


def predict_failure_probability(features: Features) -> float:
    score = 0.02 * features.files_changed + 0.06 * features.modules_impacted
    score += 0.21 if not features.tests_touched else 0.0
    score += 0.35 * features.historical_failure_rate
    return max(0.01, min(round(score, 3), 0.97))
