"""
Content management endpoints
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, HttpUrl

from services.content_ingestion import content_service

router = APIRouter()


class IngestURLRequest(BaseModel):
    url: HttpUrl


class IngestGitHubRequest(BaseModel):
    repo_url: str


@router.post("/ingest/url")
async def ingest_url(request: IngestURLRequest):
    """
    Ingest and analyze content from URL
    Returns metadata about the content
    """
    try:
        result = await content_service.ingest_url(str(request.url))
        return result['metadata']
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to ingest URL")


@router.post("/ingest/github")
async def ingest_github(request: IngestGitHubRequest):
    """
    Ingest and analyze GitHub repository
    Returns metadata about the repository
    """
    try:
        result = await content_service.ingest_github_repo(request.repo_url)
        return result['metadata']
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to ingest GitHub repository")
