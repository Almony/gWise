from datetime import datetime, timedelta
from typing import Optional

from pyrogram import Client
from pyrogram.types import ChatMember

from core.handlers.exception_handlers import handle_exceptions
from features.channel.analyzer.db import get_channel_config, save_channel_config
from features.channel.analyzer.schemas import ChannelConfig
from features.channel.analyzer.exceptions import AnalyzerDisabled, NotAdminError
from features.channel.analyzer.utils import get_current_utc_timestamp


class ChannelAnalyzer:
    """Main class responsible for controlling channel analytics behavior."""

    def __init__(self, chat_id: int, client: Client):
        self.chat_id = chat_id
        self.client = client
        self._config: Optional[ChannelConfig] = None

    @handle_exceptions
    async def is_bot_admin(self) -> bool:
        """
        Check if the bot is an admin in the given channel.
        """
        member: ChatMember = await self.client.get_chat_member(self.chat_id, "me")
        return member.status in ("administrator", "creator")

    async def get_config(self) -> ChannelConfig:
        """
        Load channel analyzer configuration from database.
        """
        if self._config is None:
            self._config = await get_channel_config(self.chat_id)
            if self._config is None:
                self._config = ChannelConfig(channel_id=self.chat_id)
        return self._config

    async def set_config(self, config: ChannelConfig):
        """
        Save updated analyzer configuration to database.
        """
        self._config = config
        await save_channel_config(config)

    async def is_enabled(self) -> bool:
        """
        Check if analyzer is enabled for the channel.
        """
        config = await self.get_config()
        return config.analyzer_enabled

    async def enable(self):
        """
        Enable analyzer for the channel.
        """
        config = await self.get_config()
        config.analyzer_enabled = True
        await self.set_config(config)

    async def disable(self):
        """
        Disable analyzer for the channel.
        """
        config = await self.get_config()
        config.analyzer_enabled = False
        await self.set_config(config)

    @handle_exceptions
    async def bootstrap_collect_history(self, limit: int = 300):
        """
        Collect historical posts from the channel (one-time on first enable).
        Updates history_collected and last_collection timestamp.
        """
        # Placeholder: logic will be implemented in next stage
        config = await self.get_config()
        if config.history_collected:
            return

        # ... placeholder for future history collection logic ...

        config.history_collected = True
        config.last_collection = get_current_utc_timestamp()
        await self.set_config(config)

    @handle_exceptions
    async def collect_new_posts(self):
        """
        Collect posts published since last_collection (excluding last 42 hours).
        """
        config = await self.get_config()
        if not config.analyzer_enabled:
            raise AnalyzerDisabled("Analyzer is disabled for this channel.")

        # ... placeholder for fetching new posts logic ...
        now = get_current_utc_timestamp()
        collection_limit = now - timedelta(hours=42)

        # logic to collect posts from last_collection to collection_limit

        config.last_collection = now
        await self.set_config(config)

    async def generate_report(self) -> dict:
        """
        Generate a summary report based on collected posts.
        """
        # Placeholder for report generation logic
        return {}

    async def export_json_report(self) -> dict:
        """
        Export top posts and analytics-ready format for AI.
        """
        # Placeholder for future AI export logic
        return {}
