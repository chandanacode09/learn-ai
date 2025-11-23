"""
Explanation API endpoints
"""
from fastapi import APIRouter, HTTPException, Depends
from typing import Optional

from models.schemas import (
    ExplainContentRequest, ExplanationResponse,
    FollowUpQuestion, FollowUpResponse, ContentType
)
from services.explanation_engine import explanation_engine
from services.content_ingestion import content_service

router = APIRouter()


@router.post("/explain", response_model=ExplanationResponse)
async def explain_content(request: ExplainContentRequest):
    """
    Generate explanation for content
    Supports URLs, GitHub repos, PDFs, or direct text
    """
    try:
        # Determine content source and ingest
        content = None
        content_type = ContentType.ARTICLE

        if request.url:
            # Ingest from URL
            result = await content_service.ingest_url(str(request.url))
            content = result['content']
            content_type = result['metadata']['content_type']

        elif request.github_repo:
            # Ingest GitHub repository
            result = await content_service.ingest_github_repo(request.github_repo)
            content = result['content']
            content_type = ContentType.GITHUB_REPO

        elif request.pdf_path:
            # Ingest PDF
            result = await content_service.ingest_pdf(request.pdf_path)
            content = result['content']
            content_type = ContentType.PDF

        elif request.content:
            # Use provided content directly
            content = request.content
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

        # Generate explanation
        explanation = await explanation_engine.explain(
            content=content,
            level=request.level,
            mode=request.mode,
            content_type=content_type,
            generate_visuals=request.generate_visuals,
            include_examples=request.include_examples,
            include_prerequisites=request.include_prerequisites
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
