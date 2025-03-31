from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
from typing import Optional
from core.config import settings
from core.logger import CustomLogger
from core.mongo.schemas import MongoCollections

logger = CustomLogger("MongoManager")


class MongoManager:
    def __init__(self):
        self.client = AsyncIOMotorClient(settings.MONGODB_URI)
        self.db = self.client["telegram_ai_bot"]

    def get_collection(self, name: str):
        if not hasattr(MongoCollections, name.upper()):
            logger.warning(f"Запрос к несуществующей коллекции: {name}")
        collection = self.db[name]
        logger.debug(f"Получена коллекция: {name}")
        return collection

    # === Пользователи ===

    async def get_user(self, user_id: int):
        users = self.get_collection(MongoCollections.USERS)
        return await users.find_one({"user_id": user_id})

    async def create_user(
        self,
        user_id: int,
        first_name: str,
        username: str,
        language_code: Optional[str] = None,
        is_premium: Optional[bool] = None,
        invited_by: Optional[int] = None
    ):
        users = self.get_collection(MongoCollections.USERS)
        existing = await users.find_one({"user_id": user_id})
        if existing:
            return existing

        now = datetime.utcnow()
        user_doc = {
            "user_id": user_id,
            "first_name": first_name,
            "username": username,
            "language_code": language_code or "unknown",
            "is_premium": is_premium or False,
            "created_at": now,
            "last_active_at": now,
            "subscription": {
                "type": "free",
                "ai_requests_left": 3,
                "priority": 0,
                "active": True
            },
            "subscription_history": {
                "free": [now]
            },
            "service_reminder_status": True,
            "service_finance_status": True,
            "service_group_status": False,
            "groups_ids": [],
            "chat_ids": [],
            "bot_version": "2.0"
        }

        if invited_by:
            user_doc["invited_by"] = invited_by
            await self.add_referral(invited_by, user_id)

        await users.insert_one(user_doc)
        logger.info(f"Создан новый пользователь: {user_id}")
        return user_doc

    async def update_user(self, user_id: int, data: dict):
        users = self.get_collection(MongoCollections.USERS)
        await users.update_one({"user_id": user_id}, {"$set": data})
        logger.debug(f"Обновлены данные пользователя {user_id}: {data}")

    async def track_activity(self, user_id: int):
        await self.update_user(user_id, {"last_active_at": datetime.utcnow()})

    async def add_referral(self, inviter_id: int, new_user_id: int):
        users = self.get_collection(MongoCollections.USERS)
        await users.update_one(
            {"user_id": inviter_id},
            {"$push": {
                "referrals": {
                    "user_id": new_user_id,
                    "date": datetime.utcnow()
                }
            }}
        )
        logger.debug(f"Пользователь {inviter_id} пригласил {new_user_id}")
