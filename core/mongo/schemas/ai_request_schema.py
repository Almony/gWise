# gWise/core/mongo/schemas/ai_request_schema.py

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class AIRequestSchema(BaseModel):
    user_id: int
    prompt: str
    response: Optional[str] = None
    total_tokens: int
    model_used: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
