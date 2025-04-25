# gWise/core/mongo/schemas/chat_schema.py

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ChatSchema(BaseModel):
    chat_id: int
    title: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
