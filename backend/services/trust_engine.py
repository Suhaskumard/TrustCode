import logging
from typing import Dict, Any
from .ai_analyzer import AIAnalyzer

logger = logging.getLogger(__name__)

class TrustEngine:
    def __init__(self):
        self.ai_analyzer = AIAnalyzer()
        self.weights = {
            'stars': 0.15,
            'forks': 0.10,
            'commits': 0.20,
            'issues': -0.15,
            'quality': 0.25,
            'complexity': 0.15
        }

    def calculate_trust_score(self, repo_data: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate comprehensive trust score 0-100."""
        stats = repo_data.get('stats', {})
        
        # Normalize metrics
        stars_norm = min(stats.get('stars', 0) / 1000, 1.0) * 100
        forks_norm = min(stats.get('forks', 0) / 500, 1.0) * 100
        commits_norm = min(stats.get('commits', 0) / 5000, 1.0) * 100
        
        issues_norm = max(0, 100 - (stats.get('open_issues', 0) * 2))
        
        # AI analysis
        ai_quality = self.ai_analyzer.analyze_quality(stats)
        quality_score = ai_quality.get('quality_score', 50)
        complexity_analysis = self.ai_analyzer.analyze_complexity(stats.get('files_count', 10))
        complexity_score = 100 - (complexity_analysis['cyclomatic_complexity'] * 15)

        # Weighted score
        score = (
            stars_norm * self.weights['stars'] +
            forks_norm * self.weights['forks'] +
            commits_norm * self.weights['commits'] +
            issues_norm * self.weights['issues'] * 0.01 +
            quality_score * self.weights['quality'] +
            complexity_score * self.weights['complexity']
        ) * 100  # Scale to 0-100

        score = max(0, min(100, score))

        grade = self._get_grade(score)
        
        return {
            'overall': round(score, 1),
            'factors': {
                'community': round((stars_norm + forks_norm) / 2, 1),
                'activity': round((commits_norm + issues_norm) / 2, 1),
                'quality': quality_score,
                'complexity': complexity_score
            },
            'grade': grade
        }

    def _get_grade(self, score: float) -> str:
        if score >= 90: return 'A'
        elif score >= 80: return 'B'
        elif score >= 70: return 'C'
        elif score >= 60: return 'D'
        else: return 'F'

