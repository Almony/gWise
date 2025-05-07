from typing import Optional

from pyrogram import Client
from motor.motor_asyncio import AsyncIOMotorClient

from core.system.bot_context import BotContext
from core.mongo.collections import MongoCollections
from core.logging import get_logger


class ChannelAnalyzer:
    def __init__(self, context: BotContext, channel_id: int, user_id: int) -> None:
        self.context: BotContext = context
        self.bot: Client = context.bot
        # TODO: Do I really need acces to all DB?
        self.db: AsyncIOMotorClient = context.db  # type: ignore
        self.channel_id: int = channel_id
        self.user_id: int = user_id

        # TODO: how and where should I work with collections?
        self.channel_collection = self.db[MongoCollections.CHANNELS.value]
        self.posts_collection = self.db[MongoCollections.CHANNEL_POSTS.value]

        # TODO: use custome logger
        self.logger = self.context.logger

    async def validate_access(self) -> None:
        """
        Проверяет:
        - является ли бот админом канала
        - активна ли подписка
        - включен ли анализ канала
        """
        pass  # Будет реализовано на Этапе 3

    async def collect_statistics(self) -> list[dict]:
        """
        Получает посты из канала, обрезая последние два дня.
        Возвращает список словарей с данными постов.
        """
        pass  # Будет реализовано на Этапе 4

    async def store_statistics(self, posts: list[dict]) -> None:
        """
        Удаляет старые посты и вставляет новые в MongoDB.
        """
        pass  # Будет реализовано на Этапе 5

    async def export_summary(self, top_n: int = 10, metric: str = "views", reverse: bool = True) -> str:
        """
        Генерирует краткий Markdown-отчёт по топ-N постам.
        """
        pass  # Будет реализовано на Этапе 6





"""
    async def validate_access(self) -> None:
        # 1. Проверка — бот админ?
        try:
            member = await self.bot.get_chat_member(self.channel_id, self.bot.me.id)
            if not member.can_manage_chat or not member.status == "administrator":
                raise BotNotAdminError(channel_id=self.channel_id)
        except UserNotParticipant:
            raise BotNotAdminError(channel_id=self.channel_id)

        # 2. Проверка подписки
        has_access = await self.context.subscription_checker.has_channel_access(self.user_id)
        if not has_access:
            raise SubscriptionRequiredError(user_id=self.user_id)

        # 3. Проверка: включен ли анализ
        channel_doc = await self.channel_collection.find_one({"channel_id": self.channel_id})
        if not channel_doc or not channel_doc.get("analyzer_enabled", False):
            raise ChannelAnalyzerDisabledError(channel_id=self.channel_id)

        self.logger.info("Access validated for channel analysis.")




import asyncio
from datetime import datetime, timedelta, timezone

from pyrogram.enums import MessageMediaType
from pyrogram.types import Message


    async def collect_statistics(self) -> list[dict]:

        # Получает посты из канала, отфильтровывает по дате, приводит к общему виду.

        now = datetime.now(timezone.utc)
        cutoff_date = now - timedelta(days=2)

        # Получаем лимит по подписке
        tier_limit = await self.context.subscription_checker.get_channel_limit(self.user_id)
        self.logger.debug(f"Collecting up to {tier_limit} messages (tier limit)")

        # Хранилище результатов
        posts: list[dict] = []
        total_fetched = 0

        async for message in self.bot.get_chat_history(self.channel_id):
            if total_fetched >= tier_limit:
                break
            if not message.date or message.date > cutoff_date:
                continue
            if not self._is_valid_message(message):
                continue

            post = {
                "channel_id": self.channel_id,
                "post_id": message.id,
                "date": message.date,
                "views": message.views or 0,
                "reactions": self._count_reactions(message),
                "forwards": message.forwards or 0,
                "text": message.text or "",
                "media_type": self._detect_media_type(message)
            }
            posts.append(post)
            total_fetched += 1

        self.logger.info(f"Collected {len(posts)} messages for channel {self.channel_id}")
        return posts

    def _is_valid_message(self, message: Message) -> bool:
        return not message.empty and not message.service

    def _count_reactions(self, message: Message) -> int:
        if message.reactions:
            return sum(reaction.count for reaction in message.reactions)
        return 0

    def _detect_media_type(self, message: Message) -> str:
        if message.media is None:
            return "text"
        media = message.media.name.lower()
        if media in ["photo", "video", "document", "audio", "voice", "poll"]:
            return media
        return "other"




        from datetime import datetime, timezone


    async def store_statistics(self, posts: list[dict]) -> None:

        # Заменяет старые посты на новые в MongoDB и обновляет статус сбора.

        now = datetime.now(timezone.utc)

        # Удаляем старые посты
        delete_result = await self.posts_collection.delete_many({"channel_id": self.channel_id})
        self.logger.debug(f"Deleted {delete_result.deleted_count} old posts")

        # Вставляем новые
        if posts:
            await self.posts_collection.insert_many(posts)
            self.logger.info(f"Inserted {len(posts)} new posts")
        else:
            self.logger.warning("No posts to insert")

        # Обновляем мета-инфо в channels
        await self.channel_collection.update_one(
            {"channel_id": self.channel_id},
            {
                "$set": {
                    "last_collection": now,
                    "history_collected": True
                }
            }
        )
        self.logger.info(f"Updated collection metadata for channel {self.channel_id}")




            async def export_summary(
        self,
        top_n: int = 10,
        metric: str = "views",
        reverse: bool = True
    ) -> str:

        # Возвращает топ-N постов канала по заданной метрике в формате Markdown.

        assert metric in {"views", "reactions", "forwards"}, "Invalid metric"

        sort_order = -1 if reverse else 1

        cursor = self.posts_collection.find(
            {"channel_id": self.channel_id},
            projection={
                "post_id": 1, "date": 1, metric: 1, "text": 1
            }
        ).sort(metric, sort_order).limit(top_n)

        results = await cursor.to_list(length=top_n)

        if not results:
            return f"_Нет данных для метрики **{metric}**_"

        lines = [f"📊 **{'Top' if reverse else 'Worst'} {top_n} по метрике `{metric}`:**"]
        for i, doc in enumerate(results, 1):
            text = (doc.get("text") or "").strip()
            preview = text[:100].replace("\n", " ") + ("…" if len(text) > 100 else "")
            count = doc.get(metric, 0)
            date_str = doc["date"].strftime("%Y-%m-%d")
            lines.append(f"{i}. **{count}** — `{date_str}` — {preview or '_без текста_'}")

        return "\n".join(lines)


"""
