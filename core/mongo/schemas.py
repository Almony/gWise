# schemas/ai_request_schema.py

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List
from uuid import uuid4

# MongoDB collections
class MongoCollections:
    USERS = "users"
    REMINDERS = "reminders"
    REMINDERS_ARCHIVE = "reminders_archive"
    FINANCE_ENTRIES = "finance_entries"
    AI_REQUESTS = "ai_requests"
    GROUPS = "groups"
    GROUP_MEMBERS = "group_members"
    GROUP_POSTS = "group_posts"
    SETTINGS = "settings"
    LOGS_SYSTEM = "logs_system"
    LOGS_USER_ACTIVITY = "logs_user_activity"


# AI reques schema
class AIRequestSchema(BaseModel):
    user_id: int
    prompt: str
    response: str
    category: str = "general"
    tokens_used: Optional[int] = None
    used_in_report: bool = False
    feedback: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)


# Finance schemas
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


# Groups schemas
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
    stats: dict = {}  # views, reactions, shares
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class GroupSchema(BaseModel):
    group_id: int
    title: str
    type: str  # chat | supergroup | channel
    owner_id: int
    admins: List[int] = []
    members_count: int = 0
    features_enabled: List[str] = []
    settings: dict = {}
    created_at: datetime = Field(default_factory=datetime.utcnow)


class SettingsSchema(BaseModel):
    key: str
    value: dict  # можно использовать как универсальный конфиг


class SystemLogSchema(BaseModel):
    level: str  # INFO, WARNING, ERROR
    event_type: str  # startup, exception, shutdown, etc
    message: str
    context: Optional[dict] = {}
    timestamp: datetime = Field(default_factory=datetime.utcnow)
