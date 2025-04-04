from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message
from core import on_message
from core.mongo import UsersRepository

@on_message(filters.command("start"))
async def start_handler(client: Client, message: Message):
    user = message.from_user
    result = await UsersRepository.create_user(user.id, user.first_name or "", user.username or "")

    subscription = result.get("subscription", {})
    tier = subscription.get("type", "free")
    tokens_left = subscription.get("tokens_left", 0)

    await message.reply(
        f"👋 Привет, {user.first_name}!\n\n"
        f"Я — AI помощник. Твоя подписка: *{tier}*.\n"
        f"Осталось токенов: *{tokens_left}*\n\n"
        f"Доступные команды:\n"
        f"/ai - общий запрос\n"
        f"/ai-finance - финансовый анализ\n"
        f"/ai-reminder - анализ напоминаний\n"
        f"/ai-group - анализ групп",
        parse_mode=ParseMode.MARKDOWN
    )
