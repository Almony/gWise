from features.subscription import manager
from core.logger import CustomLogger
from pyrogram.types import Message
from functools import wraps

logger = CustomLogger("SubscriptionMiddlewares")


def check_subscription(allowed_tiers: list[str] = None):
    """
    Проверка на соответствие уровню подписки.
    Пример: @check_subscription(["base", "pro"])
    """
    allowed_tiers = allowed_tiers or ["free", "base", "advanced", "pro"]

    def decorator(func):
        @wraps(func)
        async def wrapper(client, message: Message):
            user_id = message.from_user.id
            subscription = await manager.get_subscription(user_id)
            current_tier = subscription.get("type", "free")

            if current_tier not in allowed_tiers:
                await message.reply("🚫 Доступ запрещён для вашей подписки.")
                logger.debug(f"Подписка {current_tier} не разрешена для {user_id}")
                return

            await func(client, message)
        return wrapper
    return decorator


def check_tokens(min_required_tokens: int = 50):
    """
    Проверка на наличие достаточного количества токенов перед AI-запросом.
    Пример: @check_tokens(100)
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(client, message: Message):
            user_id = message.from_user.id
            has_tokens = await manager.has_enough_tokens(
                user_id, required_tokens=min_required_tokens
            )

            if not has_tokens:
                await message.reply(
                    "🚫 Лимит токенов исчерпан.\nОбнови подписку, чтобы продолжить использовать AI."
                )
                logger.debug(f"Недостаточно токенов у пользователя {user_id}")
                return

            await func(client, message)
        return wrapper
    return decorator
