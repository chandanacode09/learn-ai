"""
User management endpoints
"""
from fastapi import APIRouter, HTTPException
from datetime import datetime

from models.schemas import User, UserUsage

router = APIRouter()


@router.get("/usage", response_model=UserUsage)
async def get_user_usage():
    """
    Get current user's usage statistics
    """
    # TODO: Implement actual user tracking
    # For MVP, return mock data
    return UserUsage(
        total_explanations=42,
        this_month=5,
        limit=10,  # Free tier limit
        tier="free"
    )


@router.get("/me", response_model=User)
async def get_current_user():
    """
    Get current user profile
    """
    # TODO: Implement actual authentication
    # For MVP, return mock user
    return User(
        id="user_123",
        email="demo@example.com",
        name="Demo User",
        tier="free",
        explanations_used=5,
        created_at=datetime.now()
    )
