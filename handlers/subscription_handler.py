# gWise/handlers/subscription_handler.py

from pyrogram import Client, filters
from core.handlers.exception_handler import handle_exceptions
from core.system.bot_context import BotContext

def register(app: Client):
    @app.on_message(filters.command("myplan"))
    @handle_exceptions
    async def myplan_handler(client: Client, message):
        user_id = message.from_user.id
        mongo = BotContext.mongo_wrapper

        user = await mongo.find_one("users", {"user_id": user_id})

        if user:
            plan = user.get("subscription_plan", "free")
        else:
            plan = "free"

        await message.reply_text(f"📦 Ваша текущая подписка: {plan.capitalize()}")
