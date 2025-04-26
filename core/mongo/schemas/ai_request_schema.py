# gWise/core/mongo/schemas/ai_request_schema.py

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class AIRequestSchema(BaseModel):
    user_id: int
    prompt: str
    response: Optional[str] = None
    category: str = "general"
    tokens_used: Optional[int] = None
    used_in_report: bool = False
    feedback: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
