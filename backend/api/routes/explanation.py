"""
Explanation API endpoints
"""
from fastapi import APIRouter, HTTPException, Depends, Request
from typing import Optional

from models.schemas import (
    ExplainContentRequest, ExplanationResponse,
    FollowUpQuestion, FollowUpResponse, ContentType
)
from services.explanation_engine import explanation_engine
from services.content_ingestion import content_service
from services.cache_service import cache_service
from services.rate_limiter import rate_limiter

router = APIRouter()


@router.post("/explain", response_model=ExplanationResponse)
async def explain_content(request_data: ExplainContentRequest, request: Request):
    """
    Generate explanation for content
    Supports URLs, GitHub repos, PDFs, or direct text
    Includes caching and rate limiting
    """
    # Rate limiting check
    client_ip = request.client.host if request.client else "unknown"
    is_allowed, remaining = rate_limiter.is_allowed(client_ip)

    if not is_allowed:
        raise HTTPException(
            status_code=429,
            detail=f"Rate limit exceeded. Maximum {rate_limiter.requests_per_window} requests per {rate_limiter.window_minutes} minutes."
        )

    try:
        # Determine content source and ingest
        content = None
        content_type = ContentType.ARTICLE

        if request_data.url:
            # Ingest from URL
            result = await content_service.ingest_url(str(request_data.url))
            content = result['content']
            content_type = result['metadata']['content_type']

        elif request_data.github_repo:
            # Ingest GitHub repository
            result = await content_service.ingest_github_repo(request_data.github_repo)
            content = result['content']
            content_type = ContentType.GITHUB_REPO

        elif request_data.pdf_path:
            # Ingest PDF
            result = await content_service.ingest_pdf(request_data.pdf_path)
            content = result['content']
            content_type = ContentType.PDF

        elif request_data.content:
            # Use provided content directly
            content = request_data.content
            content_type = ContentType.CODE_SNIPPET

        else:
            raise HTTPException(
                status_code=400,
                detail="Must provide one of: content, url, github_repo, or pdf_path"
            )

        # Validate content length
        if not content or len(content.strip()) < 50:
            raise HTTPException(
                status_code=400,
                detail="Content is too short or empty"
            )

        # Check cache first
        cached_response = cache_service.get(
            content=content[:1000],  # Use first 1000 chars for cache key
            level=request_data.level.value,
            mode=request_data.mode.value
        )

        if cached_response:
            print(f"✅ Cache hit! Saved API call for {client_ip}")
            return ExplanationResponse(**cached_response)

        # Generate explanation (cache miss)
        explanation = await explanation_engine.explain(
            content=content,
            level=request_data.level,
            mode=request_data.mode,
            content_type=content_type,
            generate_visuals=request_data.generate_visuals,
            include_examples=request_data.include_examples,
            include_prerequisites=request_data.include_prerequisites
        )

        # Cache the response
        cache_service.set(
            content=content[:1000],
            level=request_data.level.value,
            mode=request_data.mode.value,
            data=explanation.dict()
        )

        return explanation

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Error in explain endpoint: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate explanation")


@router.post("/followup", response_model=FollowUpResponse)
async def ask_followup(request: FollowUpQuestion):
    """
    Ask follow-up questions about a previous explanation
    """
    try:
        # TODO: Retrieve original explanation from database
        # For now, we'll just answer the question directly
        answer = await explanation_engine.answer_followup(
            original_explanation="",  # Would fetch from DB
            question=request.question
        )

        return FollowUpResponse(
            answer=answer,
            related_concepts=[]
        )

    except Exception as e:
        print(f"Error in followup endpoint: {e}")
        raise HTTPException(status_code=500, detail="Failed to answer follow-up question")


@router.get("/example")
async def get_example():
    """
    Get an example explanation
    Useful for testing and demos
    """
    example_content = """
    Retrieval Augmented Generation (RAG) is a technique that combines large language models
    with external knowledge retrieval. Instead of relying solely on the model's training data,
    RAG systems fetch relevant information from a database or document collection in real-time,
    then use that information to generate more accurate and contextual responses.
    """

    explanation = await explanation_engine.explain(
        content=example_content,
        level="intermediate",
        mode="personal",
        content_type=ContentType.ARTICLE,
        generate_visuals=True,
        include_examples=True,
        include_prerequisites=True
    )

    return explanation
