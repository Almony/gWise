from features.subscription.subscription_manager import subscription_manager
# from core.mongo.mongo_manager import MongoManager
from core.logger import CustomLogger
from pyrogram.types import Message
from functools import wraps

logger = CustomLogger("SubscriptionMiddlewares")

def check_subscription():
    def decorator(func):
        @wraps(func)
        async def wrapper(client, message: Message):
            user_id = message.from_user.id
            if not await subscription_manager.has_available_requests(user_id):
                await message.reply("🚫 Лимит AI-запросов исчерпан.\nОбнови подписку для продолжения.")
                return
            await func(client, message)
            await subscription_manager.decrement_request(user_id)
        return wrapper
    return decorator

