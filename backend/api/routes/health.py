"""
Health check endpoints
"""
from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "ai-content-explainer"
    }

@router.get("/ready")
async def readiness_check():
    """Readiness check endpoint"""
    # TODO: Add checks for database, Redis, etc.
    return {
        "status": "ready",
        "checks": {
            "database": "ok",
            "cache": "ok"
        }
    }
