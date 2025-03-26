from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings
from core.logger import CustomLogger

logger = CustomLogger("MongoManager")

class MongoManager:
    def __init__(self):
        self.client = AsyncIOMotorClient(settings.MONGODB_URI)
        self.db = self.client["telegram_ai_bot"]

    def get_collection(self, name: str):
        return self.db[name]

    async def get_user(self, user_id: int):
        users = self.get_collection("users")
        return await users.find_one({"user_id": user_id})

    async def create_user(self, user_id: int, first_name: str, username: str):
        users = self.get_collection("users")
        existing = await users.find_one({"user_id": user_id})
        if existing:
            return existing
        user_doc = {
            "user_id": user_id,
            "first_name": first_name,
            "username": username,
            "subscription": {
                "type": "free",
                "ai_requests_left": 3,
                "priority": 0
            }
        }
        await users.insert_one(user_doc)
        logger.info(f"Создан новый пользователь: {user_id}")
        return user_doc
