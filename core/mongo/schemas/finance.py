from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class Category(BaseModel):
    """
    Category is a core class used to encapsulate related functionality.
    """

    main: str
    sub: Optional[str] = None


class FinanceEntrySchema(BaseModel):
    """
    FinanceEntrySchema defines the structure and validation rules for a specific MongoDB document.
    """

    user_id: int
    amount: float
    category: Category
    category_group: str
    description: Optional[str] = ""
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    is_recurring: bool = False
    interval: Optional[str] = None
