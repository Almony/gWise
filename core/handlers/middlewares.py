from functools import wraps
from typing import Callable, Awaitable
from datetime import datetime

from pyrogram.types import Message, CallbackQuery

from core.system.bot_context import BotContext
from exceptions.business_exceptions import TokenLimitExceeded, SubscriptionRequired

SUBSCRIPTION_TOKEN_LIMITS = {
    "free": 10_000,
    "base": 60_000,
    "advanced": 150_000,
    "pro": 400_000,
}

def check_subscription(func: Callable[..., Awaitable]) -> Callable[..., Awaitable]:
    """
    Middleware-декоратор для проверки подписки и лимита токенов.
    """

    @wraps(func)
    async def wrapper(client, update: Message | CallbackQuery, *args, **kwargs):
        user_id = update.from_user.id
        mongo = BotContext.mongo_wrapper
        logger = BotContext.logger

        user = await mongo.find_one("users", {"user_id": user_id})
        if not user:
            raise SubscriptionRequired("Пользователь не зарегистрирован. Используйте /start.")

        subscription_plan = user.get("subscription_plan", "free")
        tokens_used = user.get("tokens_used", 0)

        limit = SUBSCRIPTION_TOKEN_LIMITS.get(subscription_plan, 0)

        if tokens_used >= limit:
            logger.warning(f"User {user_id} превысил лимит токенов для плана {subscription_plan}.")
            raise TokenLimitExceeded("Вы израсходовали лимит токенов для вашего плана. Обновите подписку.")

        return await func(client, update, *args, **kwargs)

    return wrapper
