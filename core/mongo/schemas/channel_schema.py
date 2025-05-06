# gWise/core/mongo/schemas/channel_schema.py

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List, Literal


class ChannelSchema(BaseModel):
    channel_id: int
    title: str
    username: Optional[str] = None
    owner_id: int
    analyzer_enabled: bool = False
    last_collection: Optional[datetime] = None
    history_collected: bool = False

    class Config:
        schema_extra = {
            "example": {
                "channel_id": 123456789,
                "title": "My Channel",
                "username": "mychannel",
                "owner_id": 987654321,
                "analyzer_enabled": True,
                "last_collection": "2025-05-04T00:00:00Z",
                "history_collected": True
            }
        }


class ChannelPostSchema(BaseModel):
    channel_id: int
    post_id: int
    date: datetime
    views: int
    reactions: int
    forwards: int
    text: Optional[str] = None
    media_type: Literal["text", "photo", "video", "document", "audio", "voice", "poll", "other"]

    class Config:
        schema_extra = {
            "example": {
                "channel_id": 123456789,
                "post_id": 54321,
                "date": "2025-05-04T14:00:00Z",
                "views": 1200,
                "reactions": 32,
                "forwards": 10,
                "text": "Some post content",
                "media_type": "text"
            }
        }


class ChannelStats(BaseModel):
    channel_id: int
    collected_at: datetime
    posts: List[ChannelPostSchema]
    avg_views: Optional[int] = None
    top_post: Optional[ChannelPostSchema] = None


class ChannelConfig(BaseModel):
    channel_id: int
    analyzer_enabled: bool = True
    history_collected: bool = False
    last_collection: Optional[datetime] = None
