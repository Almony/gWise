import os
from dotenv import load_dotenv
from enum import Enum

class DotEnv(Enum):
    API_ID = None
    API_HASH = None
    BOT_TOKEN = None
    MONGODB_URI = None
    OPENAI_API_KEY = None
    ADMIN_LOG_CHAT_ID = None
    ADMIN_IDS = None
    DEV_IDS = None

    @classmethod
    def load(cls, env_file: str = ".env"):
        load_dotenv(env_file)
        for var in cls:
            value = os.getenv(var.name)
            object.__setattr__(var, "_value_", value)  # напрямую меняем value в Enum

    @classmethod
    def validate(cls):
        missing = [var.name for var in cls if not var.value]
        if missing:
            raise EnvironmentError(f"Отсутствуют обязательные переменные окружения: {missing}")
