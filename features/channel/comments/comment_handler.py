from pyrogram import Client, filters
from pyrogram.types import Message
from motor.motor_asyncio import AsyncIOMotorCollection
from core.system import BotContext
from core.mongo import MongoCollections
from datetime import datetime


class CommentHandler:
    def __init__(self, context: BotContext):
        self.context = context
        self.bot : Client = self.context.bot
        self.logger = context.logger
        # TODO: I think we need Class to manage DB
        self.db = context.db
        self.comment_collection: AsyncIOMotorCollection = self.db[MongoCollections.CHANNEL_COMMENTS]  # type: ignore
        self.post_collection: AsyncIOMotorCollection = self.db[MongoCollections.CHANNEL_POSTS]  # type: ignore

    def register_handlers(self):
        # Регистрируем хендлер только на группы (обсуждения) с текстом в треде
        self.bot.add_handler(
            self.bot.on_message(
                filters.group & filters.reply & filters.text,
                group=10
            )(self.handle_comment)
        )

    async def handle_comment(self, message: Message):
        """
        Основной обработчик входящих комментариев.
        Сохраняет комментарии и обновляет метрики по посту.

        :param message: объект комментария
        """
        try:
            if not message.reply_to_message:
                return  # Пропускаем не-thread-сообщения

            post_id = message.reply_to_message.message_id  # ID поста канала
            thread_id = message.message_thread_id
            user = message.from_user

            # TODO: Преобразовать post_id в канал+post_id (если нужно для связки)
            # TODO: Проверка прав/подписки (если нужно)

            await self.save_comment(
                chat_id=message.chat.id,
                post_id=post_id,
                user_id=user.id,
                username=user.username,
                text=message.text,
                timestamp=message.date
            )

            await self.increment_post_metrics(
                chat_id=message.chat.id,
                post_id=post_id
            )

        except Exception as e:
            self.logger.exception("Ошибка при обработке комментария")

    # TODO: We already have schemas, use schemas
    async def save_comment(self, chat_id: int, post_id: int, user_id: int, username: str, text: str, timestamp: datetime):
        """
        Сохраняет комментарий в коллекции channel_comments.

        :param chat_id: ID группы-обсуждения
        :param post_id: ID поста, к которому относится комментарий
        :param user_id: ID пользователя
        :param username: username (может быть None)
        :param text: текст комментария
        :param timestamp: время создания комментария
        """
        try:
            # TODO: use MongoSchemas
            doc = {
            #     "chat_id": chat_id,
            #     "post_id": post_id,
            #     "user_id": user_id,
            #     "username": username,
            #     "text": text,
            #     "created_at": timestamp,
            }
            await self.comment_collection.insert_one(doc)
        except Exception as e:
            self.logger.exception("Ошибка при сохранении комментария")

    async def increment_post_metrics(self, chat_id: int, post_id: int):
        """
        Инкрементирует счётчик комментариев у поста в коллекции channel_posts.

        :param chat_id: ID канала
        :param post_id: ID поста
        """
        try:
            await self.post_collection.update_one(
                {"chat_id": chat_id, "post_id": post_id},
                {
                    "$inc": {"comment_count": 1},
                    "$setOnInsert": {"created_at": datetime.utcnow()}
                },
                upsert=True
            )
        except Exception as e:
            self.logger.warning(f"Не удалось обновить метрики для поста {post_id}: {e}")

    async def delete_comment(self, message: Message):
        """
        Удаляет конкретный комментарий из чата (по команде или фильтру).

        :param message: объект комментария
        """
        try:
            await self.bot.delete_messages(chat_id=message.chat.id, message_ids=[message.id])
        except Exception as e:
            self.logger.warning(f"Ошибка удаления комментария: {e}")

    async def analyze_thread(self, thread_id: int):
        """
        Заготовка: анализ активности в треде (например, вовлечённость, ключевые слова и т.п.)

        :param thread_id: ID ветки обсуждения (message_thread_id)
        """
        # TODO: выборка всех комментариев по thread_id (если сохраняется) или post_id
        # TODO: анализ и построение отчёта
        pass
