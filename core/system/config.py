import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    MONGODB_URI = os.getenv("MONGODB_URI")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ADMIN_LOG_CHAT_ID = os.getenv("ADMIN_LOG_CHAT_ID")
    ADMIN_IDS = os.getenv("ADMIN_IDS")
    DEV_IDS = os.getenv("DEV_IDS")

settings = Settings()
