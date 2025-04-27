# gWise/handlers/start_handler.py

from pyrogram import Client, filters
from core.handlers.exception_handler import handle_exceptions
from core.system.bot_context import BotContext
from core.mongo.schemas.user_schema import UserSchema
from pymongo.errors import DuplicateKeyError

"""
    user_id: int
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    language_code: Optional[str] = None
    subscription_plan: str = "free"
    tokens_used: int = 0

"""
def register(app: Client):
    @app.on_message(filters.command("start"))
    @handle_exceptions
    async def start_handler(client: Client, message):
        user_id = message.from_user.id
        username = message.from_user.username
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        language_code = message.from_user.language_code
        mongo = BotContext.mongo_wrapper


        user = UserSchema(
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            language_code=language_code,
        )
        await mongo.insert_one("users", user.dict())
        BotContext.logger.info(f"Создан новый пользователь: {user_id}")


        await message.reply_text(
            "👋 Привет! Я gWise Бот.\n\n"
            "Я помогу тебе анализировать каналы, группы и чаты с помощью AI.\n"
            "Попробуй команду /help чтобы узнать больше."
        )
