# gWise/handlers/help_handler.py

from pyrogram import Client, filters
from core.handlers.exception_handler import handle_exceptions

def register(app: Client):
    @app.on_message(filters.command("help"))
    @handle_exceptions
    async def help_handler(client: Client, message):
        help_text = (
            "🛠 Доступные команды:\n"
            "/start - Начать работу\n"
            "/help - Справка\n"
            "/myplan - Моя подписка\n"
            "/analyze - Проанализировать канал/группу\n"
            "/stats - Статистика чата"
        )
        await message.reply_text(help_text)
