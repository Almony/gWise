# gWise/core/system/bot_context.py

from pyrogram import Client
from motor.motor_asyncio import AsyncIOMotorClient
from core.system.bot_env import BotEnv, DotEnvVars
from core.logging.logger import CustomLogger
from core.mongo.mongo_client import MongoClientWrapper
from features.ai.assistant import AIClient

class BotContext:
    bot: Client = None
    mongo_client: AsyncIOMotorClient = None  # type: ignore
    db = None
    config = None
    logger = None
    mongo_wrapper: MongoClientWrapper = None
    ai_client: AIClient = None

    @classmethod
    def init(cls):
        BotEnv.load()

        cls.mongo_client = AsyncIOMotorClient(BotEnv.get(DotEnvVars.MONGODB_URI.value))
        cls.db = cls.mongo_client.get_default_database()
        cls.mongo_wrapper = MongoClientWrapper(cls.db)

        cls.logger = CustomLogger("gWise")

        cls.ai_client = AIClient(
            api_key=BotEnv.get(DotEnvVars.OPENAI_API_KEY.value),
            mongo_wrapper=cls.mongo_wrapper,
            logger=cls.logger
        )

        cls.bot = Client(
            "gWise",
            api_id=int(BotEnv.get(DotEnvVars.API_ID.value)),
            api_hash=BotEnv.get(DotEnvVars.API_HASH.value),
            bot_token=BotEnv.get(DotEnvVars.BOT_TOKEN.value),
            plugins=None
        )
