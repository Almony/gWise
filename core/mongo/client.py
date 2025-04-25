from motor.motor_asyncio import AsyncIOMotorClient
from core.system.config import settings

# TODO: Should I close connection? Any way it should be a class
client = AsyncIOMotorClient(settings.MONGODB_URI)
db = client["telegram_ai_bot"]
