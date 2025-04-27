# gWise/core/system/bot_env.py

import os
from dotenv import load_dotenv
from enum import Enum
from core.handlers import handle_exceptions


load_dotenv()

class DotEnv(str, Enum):
    API_ID = os.getenv("API_ID", "")
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    MONGODB_URI = os.getenv("MONGODB_URI", "")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    ADMIN_LOG_CHAT_ID = os.getenv("ADMIN_LOG_CHAT_ID", "")
    ADMIN_IDS = os.getenv("ADMIN_IDS", "")
    DEV_IDS = os.getenv("DEV_IDS", "")

    @classmethod
    @handle_exceptions
    def validate(cls):
        missing = [var.name for var in cls if not var.value]
        if missing:
            raise EnvironmentError(f"Missing required environment variables: {missing}")
