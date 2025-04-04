from core.mongo.mongo_manager import MongoManager
from core.logger import CustomLogger
from pyrogram.types import Message
from functools import wraps

logger = CustomLogger("SubscriptionManager")

# Обновлённые лимиты по токенам
SUBSCRIPTION_TIERS = {
    "free": {"tokens_limit": 10_000, "priority": 0, "months_limit": 1},
    "base": {"tokens_limit": 60_000, "priority": 1, "months_limit": 3},
    "advanced": {"tokens_limit": 150_000, "priority": 1, "months_limit": 3},
    "pro": {"tokens_limit": 400_000, "priority": 2, "months_limit": 6},
}

class SubscriptionManager:
    def __init__(self):
        self.mongo = MongoManager()

    async def get_subscription(self, user_id: int):
        user = await self.mongo.get_user(user_id)
        return user.get("subscription", {})

    async def decrement_tokens(self, user_id: int, tokens_used: int):
        users = self.mongo.get_collection("users")
        await users.update_one(
            {"user_id": user_id},
            {"$inc": {"subscription.tokens_left": -tokens_used}}
        )

    async def has_enough_tokens(self, user_id: int, required_tokens: int) -> bool:
        sub = await self.get_subscription(user_id)
        return sub.get("tokens_left", 0) >= required_tokens

    def get_month_limit(self, subscription_type: str) -> int:
        return SUBSCRIPTION_TIERS.get(subscription_type, {}).get("months_limit", 1)

    def get_tokens_limit(self, subscription_type: str) -> int:
        return SUBSCRIPTION_TIERS.get(subscription_type, {}).get("tokens_limit", 0)

subscription_manager = SubscriptionManager()


# TODO: Интеграция с Telegram Payments или Stripe
# TODO: Обновление подписки по webhook / вручную
# TODO: Рассылки и уведомления о скором окончании
