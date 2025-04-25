# gWise/core/mongo/schemas/user_schema.py

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class UserSchema(BaseModel):
    user_id: int
    username: Optional[str] = None
    full_name: Optional[str] = None
    language_code: Optional[str] = None
    subscription_plan: str = "free"
    tokens_used: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
