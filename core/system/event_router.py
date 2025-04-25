# gWise/core/system/event_router.py

from pyrogram import Client
from pyrogram.handlers import MessageHandler, CallbackQueryHandler

from handlers import gpt_handler

def register_all(app: Client) -> None:
    """
    Регистрация всех событий Pyrogram.
    Каждый модуль должен вызывать свою функцию регистрации здесь.
    """
    from handlers import start_handler, help_handler, subscription_handler, gpt_handler

    start_handler.register(app)
    help_handler.register(app)
    subscription_handler.register(app)
    gpt_handler.register(app)

    # Можно расширять регистрацию других событий здесь
