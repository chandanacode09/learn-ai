"""
Pydantic models for request/response validation
"""
from pydantic import BaseModel, HttpUrl, Field
from typing import Optional, List, Dict, Any
from enum import Enum
from datetime import datetime

class ExplanationLevel(str, Enum):
    """Explanation complexity levels"""
    ELI5 = "eli5"  # Explain like I'm 5
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"

class ContentType(str, Enum):
    """Supported content types"""
    ARTICLE = "article"
    GITHUB_REPO = "github_repo"
    PDF = "pdf"
    DOCUMENTATION = "documentation"
    CODE_SNIPPET = "code_snippet"

class ExplanationMode(str, Enum):
    """Explanation modes for different use cases"""
    PERSONAL = "personal"  # Quick, conversational
    EDUCATIONAL = "educational"  # Detailed, with examples
    PROFESSIONAL = "professional"  # Technical, actionable

# Request Models
class ExplainContentRequest(BaseModel):
    """Request to explain content"""
    content: Optional[str] = None
    url: Optional[HttpUrl] = None
    github_repo: Optional[str] = None
    pdf_path: Optional[str] = None

    level: ExplanationLevel = ExplanationLevel.INTERMEDIATE
    mode: ExplanationMode = ExplanationMode.PERSONAL

    generate_visuals: bool = False
    include_examples: bool = True
    include_prerequisites: bool = True

    class Config:
        json_schema_extra = {
            "example": {
                "url": "https://example.com/article",
                "level": "intermediate",
                "mode": "personal",
                "generate_visuals": True
            }
        }

class ConceptExtraction(BaseModel):
    """Extracted concept from content"""
    name: str
    description: str
    difficulty: str
    prerequisites: List[str] = []

class VisualAid(BaseModel):
    """Visual aid representation"""
    type: str  # diagram, flowchart, concept_map
    description: str
    mermaid_code: Optional[str] = None

class ExplanationResponse(BaseModel):
    """Response containing explanation"""
    id: str
    content_type: ContentType
    original_title: Optional[str] = None

    # Main explanation
    summary: str
    detailed_explanation: str
    key_takeaways: List[str]

    # Additional insights
    concepts: List[ConceptExtraction] = []
    prerequisites: List[str] = []
    visual_aids: List[VisualAid] = []
    examples: List[str] = []

    # Metadata
    level: ExplanationLevel
    mode: ExplanationMode
    estimated_read_time: int  # in minutes
    created_at: datetime

    class Config:
        json_schema_extra = {
            "example": {
                "id": "exp_123",
                "content_type": "article",
                "summary": "RAG lets Spring Boot apps answer questions using your own documents",
                "detailed_explanation": "...",
                "key_takeaways": ["RAG combines LLMs with custom data", "..."],
                "level": "intermediate",
                "mode": "personal",
                "estimated_read_time": 5
            }
        }

class FollowUpQuestion(BaseModel):
    """Follow-up question on explanation"""
    explanation_id: str
    question: str

class FollowUpResponse(BaseModel):
    """Response to follow-up question"""
    answer: str
    related_concepts: List[str] = []

# User Models
class UserCreate(BaseModel):
    """User creation request"""
    email: str
    password: str
    name: Optional[str] = None

class User(BaseModel):
    """User model"""
    id: str
    email: str
    name: Optional[str]
    tier: str = "free"  # free, pro, team, enterprise
    explanations_used: int = 0
    created_at: datetime

    class Config:
        from_attributes = True

class UserUsage(BaseModel):
    """User usage statistics"""
    total_explanations: int
    this_month: int
    limit: int
    tier: str

# Content Models
class ContentMetadata(BaseModel):
    """Metadata about ingested content"""
    id: str
    type: ContentType
    source_url: Optional[str] = None
    title: str
    author: Optional[str] = None
    published_date: Optional[datetime] = None
    word_count: int
    difficulty_score: float
    topics: List[str] = []
