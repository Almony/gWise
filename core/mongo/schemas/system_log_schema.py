from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class SystemLogSchema(BaseModel):
    """
    SystemLogSchema defines the structure and validation rules for a specific MongoDB document.
    """

    level: str
    event_type: str
    message: str
    context: Optional[dict] = {}
    timestamp: datetime = Field(default_factory=datetime.utcnow)
