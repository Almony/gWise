"""
These schemas defins the structure and validation rules for a specific MongoDB document.
"""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List


class GroupMemberSchema(BaseModel):
    group_id: int
    user_id: int
    username: Optional[str]
    language_code: Optional[str]
    is_premium: Optional[bool] = False
    joined_at: datetime = Field(default_factory=datetime.utcnow)
    invited_by: Optional[int] = None
    last_reaction_at: Optional[datetime] = None
    last_comment_at: Optional[datetime] = None
    last_share_at: Optional[datetime] = None


class GroupPostSchema(BaseModel):
    group_id: int
    post_id: int
    author_id: Optional[int]
    message_id: Optional[int]
    text: Optional[str]
    media_type: Optional[str]
    stats: dict = {}
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class GroupSchema(BaseModel):
    group_id: int
    title: str
    type: str
    owner_id: int
    admins: List[int] = []
    members_count: int = 0
    features_enabled: List[str] = []
    settings: dict = {}
    created_at: datetime = Field(default_factory=datetime.utcnow)
