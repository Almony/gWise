# gWise/core/system/bot_context.py

from pyrogram import Client
from motor.motor_asyncio import AsyncIOMotorClient
from core.system import DotEnv
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
        DotEnv.load()
        DotEnv.validate()

        cls.mongo_client = AsyncIOMotorClient(DotEnv.MONGODB_URI.value)
        cls.db = cls.mongo_client[DotEnv.GWISE_MONGODB.value]
        cls.mongo_wrapper = MongoClientWrapper(cls.db)

        cls.logger = CustomLogger("gWise")

        cls.ai_client = AIClient(
            api_key=DotEnv.OPENAI_API_KEY.value,
            mongo_wrapper=cls.mongo_wrapper,
            logger=cls.logger
        )

        cls.bot = Client(
            "gWise",
            api_id=int(DotEnv.API_ID.value),
            api_hash=DotEnv.API_HASH.value,
            bot_token=DotEnv.BOT_TOKEN.value,
            plugins=None
        )
