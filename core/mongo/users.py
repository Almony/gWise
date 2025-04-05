from datetime import datetime
from typing import Optional
from core.mongo.base import get_collection
from core.logging.logger import CustomLogger

logger = CustomLogger("UsersRepository")

SUBSCRIPTION_TOKEN_LIMITS = {
    "free": 10_000,
    "base": 60_000,
    "advanced": 150_000,
    "pro": 400_000,
}


class UsersRepository:

    @staticmethod
    async def get_user(user_id: int):
        users = get_collection("users")
        return await users.find_one({"user_id": user_id})

    @staticmethod
    async def create_user(
        user_id: int,
        first_name: str,
        username: str,
        language_code: Optional[str] = None,
        is_premium: Optional[bool] = None,
        invited_by: Optional[int] = None
    ):
        users = get_collection("users")
        existing = await users.find_one({"user_id": user_id})
        if existing:
            return existing

        now = datetime.utcnow()
        subscription_type = "free"
        tokens = SUBSCRIPTION_TOKEN_LIMITS[subscription_type]

        user_doc = {
            "user_id": user_id,
            "first_name": first_name,
            "username": username,
            "language_code": language_code or "unknown",
            "is_premium": is_premium or False,
            "created_at": now,
            "last_active_at": now,
            "subscription": {
                "type": subscription_type,
                "tokens_left": tokens,
                "priority": 0,
                "active": True
            },
            "subscription_history": {
                subscription_type: [now]
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
            await UsersRepository.add_referral(invited_by, user_id)

        await users.insert_one(user_doc)
        logger.info(f"Создан новый пользователь: {user_id}")
        return user_doc

    @staticmethod
    async def update_user(user_id: int, data: dict):
        users = get_collection("users")
        await users.update_one({"user_id": user_id}, {"$set": data})
        logger.debug(f"Обновлены данные пользователя {user_id}: {data}")

    @staticmethod
    async def track_activity(user_id: int):
        await UsersRepository.update_user(user_id, {"last_active_at": datetime.utcnow()})

    @staticmethod
    async def add_referral(inviter_id: int, new_user_id: int):
        users = get_collection("users")
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
