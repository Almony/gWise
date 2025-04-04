from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class Category(BaseModel):
    main: str
    sub: Optional[str] = None


class FinanceEntrySchema(BaseModel):
    user_id: int
    amount: float
    category: Category
    category_group: str
    description: Optional[str] = ""
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    is_recurring: bool = False
    interval: Optional[str] = None
