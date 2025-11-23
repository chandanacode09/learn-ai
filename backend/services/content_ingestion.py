"""
Content Ingestion Services
Handles extraction and processing of content from various sources
"""
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
from typing import Optional, Dict
import re
from github import Github

from core.config import settings
from models.schemas import ContentType, ContentMetadata


class ContentIngestionService:
    """Service for ingesting content from various sources"""

    def __init__(self):
        self.github_client = Github() if not settings.OPENAI_API_KEY else None

    async def ingest_url(self, url: str) -> Dict[str, str]:
        """
        Ingest content from a URL
        Returns: Dict with 'content' and 'metadata'
        """
        try:
            # Fetch the URL
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            # Parse HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract title
            title = soup.find('title')
            title_text = title.get_text() if title else "Untitled"

            # Remove script and style elements
            for script in soup(["script", "style", "nav", "footer", "header"]):
                script.decompose()

            # Get main content
            # Try to find article or main content
            main_content = (
                soup.find('article') or
                soup.find('main') or
                soup.find('div', class_=re.compile('content|article|post|body', re.I)) or
                soup.find('body')
            )

            if main_content:
                text = main_content.get_text(separator='\n', strip=True)
            else:
                text = soup.get_text(separator='\n', strip=True)

            # Clean up text
            text = self._clean_text(text)

            # Extract metadata
            metadata = {
                'title': title_text,
                'url': url,
                'word_count': len(text.split()),
                'content_type': ContentType.ARTICLE
            }

            return {
                'content': text,
                'metadata': metadata
            }

        except Exception as e:
            print(f"Error ingesting URL {url}: {e}")
            raise ValueError(f"Failed to fetch content from URL: {str(e)}")

    async def ingest_github_repo(self, repo_url: str) -> Dict[str, str]:
        """
        Ingest GitHub repository
        Analyzes README, main files, and structure
        """
        try:
            # Extract owner/repo from URL
            # e.g., https://github.com/owner/repo -> owner/repo
            parts = repo_url.rstrip('/').split('/')
            if len(parts) < 2:
                raise ValueError("Invalid GitHub URL")

            owner = parts[-2]
            repo_name = parts[-1]
            repo_identifier = f"{owner}/{repo_name}"

            # Fetch repo info via API
            api_url = f"https://api.github.com/repos/{repo_identifier}"
            response = requests.get(api_url)
            response.raise_for_status()

            repo_data = response.json()

            # Fetch README
            readme_url = f"https://raw.githubusercontent.com/{repo_identifier}/main/README.md"
            readme_response = requests.get(readme_url)

            if readme_response.status_code != 200:
                # Try master branch
                readme_url = f"https://raw.githubusercontent.com/{repo_identifier}/master/README.md"
                readme_response = requests.get(readme_url)

            readme_content = readme_response.text if readme_response.status_code == 200 else ""

            # Build repository overview
            content = f"""# {repo_data.get('name', 'Repository')}

**Description**: {repo_data.get('description', 'No description')}

**Language**: {repo_data.get('language', 'Not specified')}
**Stars**: {repo_data.get('stargazers_count', 0)}
**Forks**: {repo_data.get('forks_count', 0)}

## README

{readme_content}
"""

            metadata = {
                'title': repo_data.get('name'),
                'url': repo_url,
                'content_type': ContentType.GITHUB_REPO,
                'word_count': len(content.split()),
                'stars': repo_data.get('stargazers_count', 0),
                'language': repo_data.get('language')
            }

            return {
                'content': content,
                'metadata': metadata
            }

        except Exception as e:
            print(f"Error ingesting GitHub repo {repo_url}: {e}")
            raise ValueError(f"Failed to fetch GitHub repository: {str(e)}")

    async def ingest_pdf(self, pdf_path: str) -> Dict[str, str]:
        """
        Ingest PDF file
        """
        try:
            reader = PdfReader(pdf_path)

            # Extract text from all pages
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"

            # Clean up text
            text = self._clean_text(text)

            metadata = {
                'title': pdf_path.split('/')[-1],
                'content_type': ContentType.PDF,
                'word_count': len(text.split()),
                'pages': len(reader.pages)
            }

            return {
                'content': text,
                'metadata': metadata
            }

        except Exception as e:
            print(f"Error ingesting PDF {pdf_path}: {e}")
            raise ValueError(f"Failed to read PDF file: {str(e)}")

    def _clean_text(self, text: str) -> str:
        """Clean and normalize text"""
        # Remove excessive whitespace
        text = re.sub(r'\n\s*\n', '\n\n', text)
        text = re.sub(r' +', ' ', text)

        # Remove very short lines (likely navigation/UI elements)
        lines = text.split('\n')
        cleaned_lines = [
            line for line in lines
            if len(line.strip()) > 3 or line.strip() == ''
        ]

        return '\n'.join(cleaned_lines).strip()


# Singleton instance
content_service = ContentIngestionService()
