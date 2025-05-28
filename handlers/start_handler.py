# gWise/handlers/start_handler.py

from pyrogram import Client, filters
from pyrogram.types import Message
from core.handlers import handle_exceptions
from core.system import BotContext
from core.mongo.schemas import UserSchema
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
    async def start_handler(client: Client, message: Message) -> None:
        mongo = BotContext.mongo_wrapper

        user = UserSchema(
            user_id = message.from_user.id,
            username = message.from_user.username,
            first_name = message.from_user.first_name,
            last_name = message.from_user.last_name,
            language_code = message.from_user.language_code
        )
        is_inserted = await mongo.insert_unique("users", user.dict())
        if is_inserted:
            BotContext.logger.info(f"Создан новый пользователь: {user.user_id}")
            await message.reply_text("👋 Привет! Я gWise Бот.")
        else:
            BotContext.logger.info(f"User {user.user_id} already exists in DB")
            await message.reply_text("👋 С возвращением!")
