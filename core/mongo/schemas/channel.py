from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class ChannelPost(BaseModel):
    message_id: int
    text: Optional[str]
    views: Optional[int]
    reactions: Optional[dict]
    forwards: Optional[int]
    date: datetime

class ChannelStats(BaseModel):
    channel_id: int
    collected_at: datetime
    posts: List[ChannelPost]
    avg_views: Optional[int] = None
    top_post: Optional[ChannelPost] = None

class ChannelConfig(BaseModel):
    channel_id: int
    analyzer_enabled: bool = True
    history_collected: bool = False
    last_collection: Optional[datetime] = None
