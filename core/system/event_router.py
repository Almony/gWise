from pyrogram import Client
from typing import Callable, List, Tuple
from core.logging.logger import CustomLogger

class EventRouter:
    def __init__(self):
        self.message_handlers: List[Tuple] = []
        self.callback_query_handlers: List[Tuple] = []
        self.edited_message_handlers: List[Tuple] = []
        self.logger =  CustomLogger(name="EventRouter")

    # === Декораторы ===
    def on_message(self, *args, **kwargs):
        def wrapper(func: Callable):
            self.message_handlers.append((args, kwargs, func))
            return func
        return wrapper

    def on_callback_query(self, *args, **kwargs):
        def wrapper(func: Callable):
            self.callback_query_handlers.append((args, kwargs, func))
            return func
        return wrapper

    def on_edited_message(self, *args, **kwargs):
        def wrapper(func: Callable):
            self.edited_message_handlers.append((args, kwargs, func))
            return func
        return wrapper

    # === Регистрация всех хендлеров ===
    def register_all(self, app: Client):
        for args, kwargs, func in self.message_handlers:
            app.on_message(*args, **kwargs)(func)

        for args, kwargs, func in self.callback_query_handlers:
            app.on_callback_query(*args, **kwargs)(func)

        for args, kwargs, func in self.edited_message_handlers:
            app.on_edited_message(*args, **kwargs)(func)

        self.logger.info("All handlers registered")


# Глобальный экземпляр
event_router = EventRouter()

# Быстрый доступ к декораторам
on_message = event_router.on_message
on_callback_query = event_router.on_callback_query
on_edited_message = event_router.on_edited_message
register_all = event_router.register_all
