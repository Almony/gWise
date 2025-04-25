# gWise/handlers/start_handler.py

from pyrogram import Client, filters
from core.handlers.exception_handler import handle_exceptions
from core.system.bot_context import BotContext
from core.mongo.schemas.user_schema import UserSchema
from pymongo.errors import DuplicateKeyError


def register(app: Client):
    @app.on_message(filters.command("start"))
    @handle_exceptions
    async def start_handler(client: Client, message):
        user_id = message.from_user.id
        username = message.from_user.username
        full_name = message.from_user.first_name
        language_code = message.from_user.language_code

        mongo = BotContext.mongo_wrapper

        try:
            user = UserSchema(
                user_id=user_id,
                username=username,
                full_name=full_name,
                language_code=language_code,
            )
            await mongo.insert_one("users", user.dict())
            BotContext.logger.info(f"Создан новый пользователь: {user_id}")
        except DuplicateKeyError:
            BotContext.logger.info(f"Пользователь уже существует: {user_id}")

        await message.reply_text(
            "👋 Привет! Я gWise Бот.\n\n"
            "Я помогу тебе анализировать каналы, группы и чаты с помощью AI.\n"
            "Попробуй команду /help чтобы узнать больше."
        )
