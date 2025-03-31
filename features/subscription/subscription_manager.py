from core.mongo.mongo_manager import MongoManager
from core.logger import CustomLogger
from pyrogram.types import Message
from functools import wraps

logger = CustomLogger("SubscriptionManager")

SUBSCRIPTION_TIERS = {
    "free": {"limit": 3, "priority": 0, "months_limit": 1},
    "base": {"limit": 10, "priority": 1, "months_limit": 3},
    "advanced": {"limit": 20, "priority": 1, "months_limit": 3},
    "pro": {"limit": 50, "priority": 2, "months_limit": 6},
}

class SubscriptionManager:
    def __init__(self):
        self.mongo = MongoManager()

    async def get_subscription(self, user_id: int):
        user = await self.mongo.get_user(user_id)
        return user.get("subscription", {})

    async def decrement_request(self, user_id: int):
        users = self.mongo.get_collection("users")
        await users.update_one(
            {"user_id": user_id},
            {"$inc": {"subscription.ai_requests_left": -1}}
        )

    async def has_available_requests(self, user_id: int) -> bool:
        sub = await self.get_subscription(user_id)
        return sub.get("ai_requests_left", 0) > 0

    def get_month_limit(self, subscription_type: str) -> int:
        return SUBSCRIPTION_TIERS.get(subscription_type, {}).get("months_limit", 1)

subscription_manager = SubscriptionManager()


# TODO: Интеграция с Telegram Payments или Stripe
# TODO: Обновление подписки по webhook / вручную
# TODO: Рассылки и уведомления о скором окончании
