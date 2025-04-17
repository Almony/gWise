from typing import List, Optional

from core.mongo.client import db
from features.channel.analyzer.schemas import ChannelPost, ChannelStats, ChannelConfig
from features.channel.analyzer.utils import get_current_utc_timestamp

CONFIG_COLLECTION = db["channel_config"]
STATS_COLLECTION = db["channel_stats"]


# ---------- CONFIGURATION ----------

async def get_channel_config(channel_id: int) -> Optional[ChannelConfig]:
    data = await CONFIG_COLLECTION.find_one({"channel_id": channel_id})
    return ChannelConfig(**data) if data else None


async def save_channel_config(config: ChannelConfig) -> None:
    await CONFIG_COLLECTION.update_one(
        {"channel_id": config.channel_id},
        {"$set": config.dict()},
        upsert=True
    )


# ---------- POSTS + STATS ----------

async def save_channel_posts(channel_id: int, posts: List[ChannelPost]) -> None:
    """
    Add posts to stats collection. Trims older entries beyond 1000.
    """
    serialized = [post.dict() for post in posts]
    await STATS_COLLECTION.update_one(
        {"channel_id": channel_id},
        {
            "$set": {
                "channel_id": channel_id,
                "collected_at": get_current_utc_timestamp(),
                "posts": serialized,
                "avg_views": _calculate_avg_views(posts),
                "top_post": _get_top_post(posts)
            }
        },
        upsert=True
    )

    # Optional: trim logic can be applied here if posts > 1000 in future


async def get_recent_channel_posts(channel_id: int, limit: int = 300) -> List[ChannelPost]:
    """
    Get last `limit` posts from the stats collection.
    """
    data = await STATS_COLLECTION.find_one({"channel_id": channel_id})
    if not data or "posts" not in data:
        return []

    posts = data["posts"][-limit:]  # Return only the latest N
    return [ChannelPost(**post) for post in posts]


async def clear_old_posts(channel_id: int, max_posts: int = 1000) -> None:
    """
    Truncate posts list to keep only the most recent `max_posts` posts.
    """
    data = await STATS_COLLECTION.find_one({"channel_id": channel_id})
    if not data or "posts" not in data:
        return

    trimmed = data["posts"][-max_posts:]
    await STATS_COLLECTION.update_one(
        {"channel_id": channel_id},
        {"$set": {"posts": trimmed}}
    )


# ---------- INTERNAL HELPERS ----------

def _calculate_avg_views(posts: List[ChannelPost]) -> int:
    views = [p.views for p in posts if p.views is not None]
    return int(sum(views) / len(views)) if views else 0


def _get_top_post(posts: List[ChannelPost]) -> Optional[dict]:
    if not posts:
        return None
    top = max(posts, key=lambda p: (p.views or 0))
    return top.dict()
