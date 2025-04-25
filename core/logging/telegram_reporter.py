# gWise/core/logging/telegram_reporter.py

import asyncio
from core.system.bot_context import BotContext
from core.system.bot_env import BotEnv

async def report_error_to_telegram(error_text: str):
    try:
        admin_chat_id = int(BotEnv.get("ADMIN_LOG_CHAT_ID"))
        if BotContext.bot.is_connected:
            await BotContext.bot.send_message(chat_id=admin_chat_id, text=f"🚨 Ошибка:\n<pre>{error_text}</pre>", parse_mode="html")
    except Exception as e:
        # Не логируем падение репортера, чтобы не создавать бесконечный цикл
        # TODO: send messages to all admins
        print(f"Telegram Reporter Failed: {e}")
