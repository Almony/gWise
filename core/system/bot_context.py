# gWise/core/system/bot_context.py

from pyrogram import Client
from motor.motor_asyncio import AsyncIOMotorClient
from core.system.bot_env import BotEnv
from core.logging.logger import CustomLogger  # <- добавили
from core.mongo.mongo_client import MongoClientWrapper

class BotContext:
    bot: Client = None
    mongo_client: AsyncIOMotorClient = None # type: ignore
    db = None
    config = None
    logger = None
    openai_client = None
    mongo_wrapper: MongoClientWrapper = None

    @classmethod
    def init(cls):
        BotEnv.load()

        cls.mongo_client = AsyncIOMotorClient(BotEnv.get("MONGODB_URI"))
        cls.db = cls.mongo_client.get_default_database()
        cls.mongo_wrapper = MongoClientWrapper(cls.db)

        cls.bot = Client(
            "gWise",
            api_id=int(BotEnv.get("API_ID")),
            api_hash=BotEnv.get("API_HASH"),
            bot_token=BotEnv.get("BOT_TOKEN"),
            plugins=None
        )

        cls.logger = CustomLogger("gWise")
