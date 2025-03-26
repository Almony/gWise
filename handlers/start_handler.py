from pyrogram import Client, filters
from pyrogram.types import Message
from core.mongo_manager import MongoManager

mongo = MongoManager()

@Client.on_message(filters.command("start"))
async def start_handler(client: Client, message: Message):
    user = message.from_user
    result = await mongo.create_user(user.id, user.first_name or "", user.username or "")
    await message.reply(
        f"👋 Привет, {user.first_name}!\n\n"
        "Я — AI помощник. Твоя подписка: *free*.\n"
        "Осталось AI-запросов: 3\n\n"
        "Доступные команды:\n"
        "/ai - общий запрос\n"
        "/ai-finance - финансовый анализ\n"
        "/ai-reminder - анализ напоминаний\n"
        "/ai-group - анализ групп",
        parse_mode="Markdown"
    )
