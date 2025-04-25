# gWise/core/mongo/schemas/group_schema.py

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class GroupSchema(BaseModel):
    group_id: int
    title: str
    analyzer_enabled: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
