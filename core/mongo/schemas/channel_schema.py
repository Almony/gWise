# gWise/core/mongo/schemas/channel_schema.py

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ChannelSchema(BaseModel):
    channel_id: int
    title: str
    analyzer_enabled: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
