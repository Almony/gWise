# gWise/core/system/bot_env.py

import os
from dotenv import load_dotenv
from enum import Enum


class DotEnvVars(Enum):
    API_ID = "API_ID"
    API_HASH = "API_HASH"
    BOT_TOKEN = "BOT_TOKEN"
    MONGODB_URI = "MONGODB_URI"
    OPENAI_API_KEY = "OPENAI_API_KEY"
    ADMIN_LOG_CHAT_ID = "ADMIN_LOG_CHAT_ID"
    ADMIN_IDS = "ADMIN_IDS"
    DEV_IDS = "DEV_IDS"


class BotEnv:

    @classmethod
    def load(cls) -> None:
        load_dotenv()

        missing_vars = [var.value for var in DotEnvVars if not os.getenv(var.value)]
        if missing_vars:
            raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")

    @classmethod
    def get(cls, key: str, default=None):
        return os.getenv(key, default)
