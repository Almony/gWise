from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class AIRequestSchema(BaseModel):
    user_id: int
    prompt: str
    response: str
    category: str = "general"
    tokens_used: Optional[int] = None
    used_in_report: bool = False
    feedback: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)
