"""
AI Content Explainer - FastAPI Backend
Main application entry point
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn

from api.routes import explanation, content, user, health
from core.config import settings
from core.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler"""
    # Startup
    print("🚀 Starting AI Content Explainer API...")

    # Validate API keys
    if not settings.OPENAI_API_KEY and not settings.ANTHROPIC_API_KEY:
        print("❌ ERROR: No AI API keys configured!")
        print("Please set either OPENAI_API_KEY or ANTHROPIC_API_KEY in your .env file")
        print("Get your OpenAI key from: https://platform.openai.com/api-keys")
        print("Get your Anthropic key from: https://console.anthropic.com/")
        raise RuntimeError("No AI API keys configured. Please add OPENAI_API_KEY or ANTHROPIC_API_KEY to .env file")

    if settings.OPENAI_API_KEY:
        print(f"✅ OpenAI API key configured ({settings.OPENAI_API_KEY[:10]}...)")
    if settings.ANTHROPIC_API_KEY:
        print(f"✅ Anthropic API key configured ({settings.ANTHROPIC_API_KEY[:10]}...)")

    await init_db()
    print("✅ Database initialized")
    print("✅ Caching enabled (24 hour TTL)")
    print(f"✅ Rate limiting: 10 requests/hour for free tier")
    print(f"✅ CORS origins: {settings.CORS_ORIGINS}")
    print(f"\n🌐 API running at http://localhost:8000")
    print(f"📖 API docs at http://localhost:8000/docs\n")

    yield

    # Shutdown
    print("👋 Shutting down API...")

# Create FastAPI app
app = FastAPI(
    title="AI Content Explainer API",
    description="API for generating multi-level explanations of technical content",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, prefix="/api/v1", tags=["Health"])
app.include_router(explanation.router, prefix="/api/v1/explanation", tags=["Explanation"])
app.include_router(content.router, prefix="/api/v1/content", tags=["Content"])
app.include_router(user.router, prefix="/api/v1/user", tags=["User"])

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "AI Content Explainer API",
        "version": "1.0.0",
        "docs": "/docs"
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.ENVIRONMENT == "development"
    )
