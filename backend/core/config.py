"""
Configuration management using Pydantic Settings
"""
from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    """Application settings"""

    # API Keys
    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""

    # Database
    DATABASE_URL: str = "sqlite:///./ai_explainer.db"
    REDIS_URL: str = "redis://localhost:6379"

    # Vector Database
    PINECONE_API_KEY: str = ""
    PINECONE_ENVIRONMENT: str = ""

    # Auth
    JWT_SECRET_KEY: str = "your-secret-key-change-in-production"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Clerk
    CLERK_API_KEY: str = ""

    # Stripe
    STRIPE_API_KEY: str = ""
    STRIPE_WEBHOOK_SECRET: str = ""

    # Application
    ENVIRONMENT: str = "development"
    API_VERSION: str = "v1"
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "chrome-extension://*"]

    # AI Model Settings
    DEFAULT_AI_MODEL: str = "gpt-4-turbo-preview"
    MAX_TOKENS: int = 2000
    TEMPERATURE: float = 0.7

    # Rate Limiting
    RATE_LIMIT_FREE_TIER: int = 10  # explanations per month
    RATE_LIMIT_PRO_TIER: int = -1  # unlimited

    class Config:
        env_file = ".env"
        case_sensitive = True

# Create settings instance
settings = Settings()
