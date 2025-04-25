# gWise/core/system/bot_context.py

from pyrogram import Client
from motor.motor_asyncio import AsyncIOMotorClient
from core.system.bot_env import BotEnv

class BotContext:
    bot: Client = None
    mongo_client: AsyncIOMotorClient = None # type: ignore
    db = None  # Основная БД
    config = None  # Будущие настройки проекта
    logger = None  # Будет подключено на следующем этапе
    openai_client = None  # Будет подключено на этапе интеграции AI

    @classmethod
    def init(cls):
        BotEnv.load()

        cls.mongo_client = AsyncIOMotorClient(BotEnv.get("MONGODB_URI"))
        cls.db = cls.mongo_client.get_default_database()

        cls.bot = Client(
            "gWise",
            api_id=int(BotEnv.get("API_ID")),
            api_hash=BotEnv.get("API_HASH"),
            bot_token=BotEnv.get("BOT_TOKEN"),
            plugins=None  # Пока без плагинов
        )
