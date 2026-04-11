from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
import os
from dotenv import load_dotenv
from models.schemas import RepoAnalysisRequest, AnalysisResponse
from utils.github_api import GitHubAPI
from services.trust_engine import TrustEngine
from services.ai_analyzer import AIAnalyzer
import uvicorn

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="TrustCode Platform API", version="1.0.0")

# CORS
origins = os.getenv("ORIGINS", '["http://localhost:3000"]').replace("'", '"').split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

github_api = GitHubAPI()
trust_engine = TrustEngine()
ai_analyzer = AIAnalyzer()

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "trustcode-platform"}

@app.post("/analyze-repo/{repo_url:path}", response_model=AnalysisResponse)
async def analyze_repo(repo_url: str):
    try:
        logger.info(f"Analyzing repo: {repo_url}")
        
        # Fetch repo data
        repo_info = await github_api.get_repo_info(repo_url)
        if not repo_info:
            raise HTTPException(status_code=400, detail="Invalid repo or no access")

        owner, repo = repo_info['full_name'].split('/')
        
        # Gather stats
        stats = {
            'stars': repo_info.get('stargazers_count', 0),
            'forks': repo_info.get('forks_count', 0),
            'open_issues': repo_info.get('open_issues_count', 0),
            'files_count': repo_info.get('size', 0) // 100,  # Approx
        }
        stats['commits'] = await github_api.get_commits(owner, repo)
        stats['open_issues'] = await github_api.get_issues(owner, repo)

        # Trust score
        trust_score = trust_engine.calculate_trust_score({'stats': stats})

        # AI insights
        insights = ai_analyzer.generate_insights(stats)
        metrics = [
            {'name': 'Stars', 'value': stats['stars'], 'max_value': 10000, 'description': 'Community interest'},
            {'name': 'Forks', 'value': stats['forks'], 'max_value': 5000, 'description': 'Community usage'},
            {'name': 'Commits', 'value': stats['commits'], 'max_value': 10000, 'description': 'Activity'},
            {'name': 'Open Issues', 'value': stats['open_issues'], 'max_value': 100, 'description': 'Maintenance'},
        ]
        
        summary = f"{repo_info['name']} has a trust score of {trust_score['overall']:.1f}/100 ({trust_score['grade']}). {insights['summary']}"
        recs = ai_analyzer.get_recommendations()

        return AnalysisResponse(
            repo_name=repo_info['name'],
            repo_url=repo_info['html_url'],
            stars=stats['stars'],
            forks=stats['forks'],
            open_issues=stats['open_issues'],
            commits=stats['commits'],
            trust_score=trust_score,
            ai_insights=insights,
            metrics=metrics,
            summary=summary,
            recommendations=recs
        )
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Analysis error: {e}")
        raise HTTPException(status_code=500, detail="Analysis failed")

@app.on_event("shutdown")
async def shutdown():
    await github_api.close()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

