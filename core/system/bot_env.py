import os
from dotenv import load_dotenv
from enum import Enum
from pathlib import Path

class DotEnv(Enum):
    API_ID = os.getenv("API_ID")
    API_HASH = os.getenv("API_HASH")
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    MONGODB_URI = os.getenv("MONGODB_URI")
    GWISE_MONGODB = os.getenv("GWISE_MONGODB")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ADMIN_LOG_CHAT_ID = os.getenv("ADMIN_LOG_CHAT_ID")
    ADMIN_IDS = os.getenv("ADMIN_IDS")
    DEV_IDS = os.getenv("DEV_IDS")

    # @classmethod
    # def load(cls, dotenv_path: str = ".env"):
    #     load_dotenv()# load_dotenv(dotenv_path=Path(dotenv_path))
    #     for item in cls:
    #         value = os.getenv(item.name)
    #         if value is not None:
    #             setattr(cls, item.name, value)
    #         else:
    #             setattr(cls, item.name, None)

    # @classmethod
    # def load(cls, env_file: str = ".env"):
    #     load_dotenv(env_file)
    #     for var in cls:
    #         value = os.getenv(var.name)
    #         object.__setattr__(var, "_value_", value)  # напрямую меняем value в Enum

    @classmethod
    def validate(cls):
        missing = [var.name for var in cls if var.value is None]
        if missing:
            raise EnvironmentError(f"Отсутствуют обязательные переменные окружения: {missing}")
