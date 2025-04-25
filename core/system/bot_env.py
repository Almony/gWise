# gWise/core/system/bot_env.py

import os
from dotenv import load_dotenv

class BotEnv:
    REQUIRED_VARS = [
        "API_ID",
        "API_HASH",
        "BOT_TOKEN",
        "MONGODB_URI",
        "OPENAI_API_KEY",
        "ADMIN_LOG_CHAT_ID",
        "ADMIN_IDS",
        "DEV_IDS",
    ]

    @classmethod
    def load(cls) -> None:
        load_dotenv()

        missing_vars = [var for var in cls.REQUIRED_VARS if not os.getenv(var)]
        if missing_vars:
            raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")

    @classmethod
    def get(cls, key: str, default=None):
        return os.getenv(key, default)
