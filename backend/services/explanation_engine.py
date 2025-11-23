"""
AI Explanation Engine - Core service for generating multi-level explanations
"""
import openai
from anthropic import Anthropic
from typing import Dict, List, Optional
import json
from datetime import datetime
import uuid

from core.config import settings
from models.schemas import (
    ExplanationLevel, ExplanationMode, ExplanationResponse,
    ConceptExtraction, VisualAid, ContentType
)

# Initialize AI clients
openai.api_key = settings.OPENAI_API_KEY
anthropic_client = Anthropic(api_key=settings.ANTHROPIC_API_KEY) if settings.ANTHROPIC_API_KEY else None


class ExplanationEngine:
    """Main engine for generating explanations"""

    def __init__(self):
        self.model = settings.DEFAULT_AI_MODEL

    async def explain(
        self,
        content: str,
        level: ExplanationLevel,
        mode: ExplanationMode,
        content_type: ContentType = ContentType.ARTICLE,
        generate_visuals: bool = False,
        include_examples: bool = True,
        include_prerequisites: bool = True
    ) -> ExplanationResponse:
        """
        Generate explanation for given content
        """
        # Build the prompt based on level and mode
        prompt = self._build_prompt(
            content, level, mode, generate_visuals,
            include_examples, include_prerequisites
        )

        # Generate explanation using AI
        response = await self._generate_with_openai(prompt)

        # Parse and structure the response
        explanation = self._parse_response(
            response, content, level, mode, content_type
        )

        return explanation

    def _build_prompt(
        self,
        content: str,
        level: ExplanationLevel,
        mode: ExplanationMode,
        generate_visuals: bool,
        include_examples: bool,
        include_prerequisites: bool
    ) -> str:
        """Build the AI prompt based on parameters"""

        # Level-specific instructions
        level_instructions = {
            ExplanationLevel.ELI5: "Explain this as if to a 5-year-old. Use simple analogies and everyday examples. Avoid technical jargon entirely.",
            ExplanationLevel.BEGINNER: "Explain this to someone new to the topic. Define technical terms when used. Use relatable analogies.",
            ExplanationLevel.INTERMEDIATE: "Explain this assuming basic familiarity with the domain. Focus on how things work and why they matter.",
            ExplanationLevel.ADVANCED: "Provide detailed technical explanation. Include implementation considerations and best practices.",
            ExplanationLevel.EXPERT: "Deep technical analysis. Discuss edge cases, performance implications, and architectural decisions."
        }

        # Mode-specific instructions
        mode_instructions = {
            ExplanationMode.PERSONAL: "Keep it conversational and friendly. Focus on 'what's the buzz about' and practical takeaways.",
            ExplanationMode.EDUCATIONAL: "Provide comprehensive learning material. Include study questions and progressive learning path.",
            ExplanationMode.PROFESSIONAL: "Focus on actionable insights, implementation effort, cost analysis, and production considerations."
        }

        prompt = f"""You are an expert technical content explainer. Your job is to make complex content accessible and understandable.

CONTENT TO EXPLAIN:
{content[:4000]}  # Limit content length

EXPLANATION LEVEL: {level.value}
{level_instructions[level]}

EXPLANATION MODE: {mode.value}
{mode_instructions[mode]}

Please provide your explanation in the following JSON format:
{{
    "summary": "One or two sentence instant insight",
    "detailed_explanation": "Comprehensive explanation following the level and mode guidelines",
    "key_takeaways": ["takeaway 1", "takeaway 2", "takeaway 3"],
    "concepts": [
        {{
            "name": "concept name",
            "description": "brief description",
            "difficulty": "beginner/intermediate/advanced",
            "prerequisites": ["prerequisite concepts"]
        }}
    ],
    "prerequisites": ["What you need to know first"],
    "examples": ["Real-world examples or use cases"],
    "visual_aids": [
        {{
            "type": "diagram/flowchart/concept_map",
            "description": "Description of what should be visualized",
            "mermaid_code": "Optional mermaid diagram code"
        }}
    ]
}}
"""

        if not include_examples:
            prompt += "\nSkip the examples section."

        if not include_prerequisites:
            prompt += "\nSkip the prerequisites section."

        if generate_visuals:
            prompt += "\nGenerate Mermaid diagram code for visual aids where helpful."

        return prompt

    async def _generate_with_openai(self, prompt: str) -> str:
        """Generate response using OpenAI"""
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful technical content explainer. Always respond with valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=settings.TEMPERATURE,
                max_tokens=settings.MAX_TOKENS,
                response_format={"type": "json_object"}  # Force JSON output
            )

            return response.choices[0].message.content
        except Exception as e:
            print(f"OpenAI API error: {e}")
            # Fallback to a simpler explanation
            return self._generate_fallback_response()

    def _generate_fallback_response(self) -> str:
        """Generate a basic fallback response if AI fails"""
        return json.dumps({
            "summary": "Unable to generate explanation. Please try again.",
            "detailed_explanation": "There was an error processing your request.",
            "key_takeaways": ["Please try again with different content"],
            "concepts": [],
            "prerequisites": [],
            "examples": [],
            "visual_aids": []
        })

    def _parse_response(
        self,
        ai_response: str,
        original_content: str,
        level: ExplanationLevel,
        mode: ExplanationMode,
        content_type: ContentType
    ) -> ExplanationResponse:
        """Parse AI response into structured format"""
        try:
            data = json.loads(ai_response)

            # Estimate read time based on word count
            word_count = len(data.get("detailed_explanation", "").split())
            estimated_read_time = max(1, word_count // 200)  # Assume 200 words/min

            # Build concept extractions
            concepts = [
                ConceptExtraction(**concept)
                for concept in data.get("concepts", [])
            ]

            # Build visual aids
            visual_aids = [
                VisualAid(**visual)
                for visual in data.get("visual_aids", [])
            ]

            return ExplanationResponse(
                id=f"exp_{uuid.uuid4().hex[:12]}",
                content_type=content_type,
                original_title=self._extract_title(original_content),
                summary=data.get("summary", ""),
                detailed_explanation=data.get("detailed_explanation", ""),
                key_takeaways=data.get("key_takeaways", []),
                concepts=concepts,
                prerequisites=data.get("prerequisites", []),
                visual_aids=visual_aids,
                examples=data.get("examples", []),
                level=level,
                mode=mode,
                estimated_read_time=estimated_read_time,
                created_at=datetime.now()
            )

        except json.JSONDecodeError as e:
            print(f"Failed to parse AI response: {e}")
            # Return a basic response
            return ExplanationResponse(
                id=f"exp_{uuid.uuid4().hex[:12]}",
                content_type=content_type,
                summary="Unable to parse explanation",
                detailed_explanation=ai_response,
                key_takeaways=[],
                level=level,
                mode=mode,
                estimated_read_time=1,
                created_at=datetime.now()
            )

    def _extract_title(self, content: str) -> Optional[str]:
        """Extract title from content (simple implementation)"""
        lines = content.split('\n')
        for line in lines[:5]:  # Check first 5 lines
            if line.strip() and len(line) < 200:
                return line.strip()
        return None

    async def answer_followup(
        self,
        original_explanation: str,
        question: str
    ) -> str:
        """Answer follow-up questions about an explanation"""
        prompt = f"""Based on this explanation:

{original_explanation[:2000]}

Please answer this follow-up question:
{question}

Provide a clear, concise answer that builds on the original explanation."""

        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful teaching assistant answering follow-up questions."},
                    {"role": "user", "content": prompt}
                ],
                temperature=settings.TEMPERATURE,
                max_tokens=500
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error answering follow-up: {e}")
            return "I'm having trouble answering that question right now. Please try again."


# Singleton instance
explanation_engine = ExplanationEngine()
