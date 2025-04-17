from typing import List, Optional
from datetime import datetime

from pyrogram import Client
from pyrogram.types import Message

from features.channel.analyzer.schemas import ChannelPost


async def fetch_channel_posts(
    client: Client,
    chat_id: int,
    limit: int = 100,
    offset_id: Optional[int] = None,
) -> List[Message]:
    """
    Fetch messages from a channel using get_chat_history.
    Returns up to `limit` messages before offset_id (if provided).
    """
    messages: List[Message] = []
    async for msg in client.get_chat_history(
        chat_id=chat_id,
        limit=limit,
        offset_id=offset_id
    ):
        if msg.date and msg.text and not msg.empty:
            messages.append(msg)
    return messages


def normalize_messages(messages: List[Message]) -> List[ChannelPost]:
    """
    Convert raw Pyrogram Message objects into ChannelPost data models.
    """
    posts: List[ChannelPost] = []

    for msg in messages:
        post = ChannelPost(
            message_id=msg.id,
            text=msg.text,
            views=msg.views or 0,
            forwards=msg.forwards or 0,
            reactions=_extract_reactions(msg),
            date=msg.date
        )
        posts.append(post)

    return posts


def _extract_reactions(msg: Message) -> Optional[dict]:
    """
    Extract recent reactions into a structured dict.
    """
    if not msg.reactions or not msg.reactions.recent_reactions:
        return None

    result = {}
    for reaction in msg.reactions.recent_reactions:
        emoji = reaction.reaction.emoticon or "unknown"
        result[emoji] = result.get(emoji, 0) + 1

    return result
