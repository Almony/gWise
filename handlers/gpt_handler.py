# gWise/handlers/gpt_handler.py

from pyrogram import Client, filters
from core.handlers.exception_handler import handle_exceptions
from core.system.bot_context import BotContext
from core.handlers.middlewares import check_subscription  # TODO: move middlewares to separated folder


def register(app: Client):
    @app.on_message(filters.command("analyze"))
    @handle_exceptions
    @check_subscription
    async def analyze_handler(client: Client, message):
        # TODO: Проанализируй активность моего канала за последний месяц.
        pass

    @app.on_message(filters.command("stats"))
    @handle_exceptions
    @check_subscription
    async def stats_handler(client: Client, message):
        await message.reply_text(
            "📊 Статистика чата в разработке! Следите за обновлениями."
        )
