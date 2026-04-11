import httpx
from typing import Dict, Any, Optional, List
import logging
from dotenv import load_dotenv
import os

load_dotenv()

logger = logging.getLogger(__name__)

class GitHubAPI:
    def __init__(self):
        self.token = os.getenv('GITHUB_TOKEN')
        self.base_url = 'https://api.github.com'
        self.headers = {
            'Authorization': f'token {self.token}' if self.token else None,
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'TrustCode-Platform/1.0'
        }
        self.client = httpx.AsyncClient(headers=self.headers, timeout=30.0)

    async def get_repo_info(self, repo_url: str) -> Optional[Dict[str, Any]]:
        """Extract owner/repo from URL and fetch repo info."""
        try:
            if '/github.com/' not in repo_url:
                raise ValueError('Invalid GitHub URL')
            owner_repo = repo_url.split('github.com/')[-1].rstrip('/').replace('/', ':')
            url = f'{self.base_url}/repos/{owner_repo}'
            resp = await self.client.get(url)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            logger.error(f'GitHub repo fetch error: {e}')
            return None

    async def get_commits(self, owner: str, repo: str, limit: int = 100) -> int:
        """Get approximate commit count."""
        try:
            url = f'{self.base_url}/repos/{owner}/{repo}/commits?per_page=1'
            resp = await self.client.get(url)
            if resp.status_code == 200:
                link_header = resp.headers.get('link', '')
                if 'last' in link_header:
                    return int(link_header.split('page=')[1].split('>')[0])
            return 0
        except:
            return 0

    async def get_issues(self, owner: str, repo: str) -> int:
        """Get open issues count."""
        try:
            url = f'{self.base_url}/repos/{owner}/{repo}/issues?state=open&per_page=1'
            resp = await self.client.get(url)
            link_header = resp.headers.get('link', '')
            if 'last' in link_header:
                return int(link_header.split('page=')[1].split('>')[0])
            return resp.json().__len__() if resp.status_code == 200 else 0
        except:
            return 0

    async def close(self):
        await self.client.aclose()

