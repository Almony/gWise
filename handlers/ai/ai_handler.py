from pyrogram import Client, filters
from pyrogram.types import Message
from ai.ai_manager import ai_manager
from subscription.subscription_manager import check_subscription

def ai_command_handler(command_name: str, category: str):
    @Client.on_message(filters.command(command_name))
    @check_subscription()
    async def handler(client: Client, message: Message):
        prompt = message.text.split(maxsplit=1)
        if len(prompt) < 2:
            await message.reply("✍️ Пожалуйста, добавь текст запроса после команды.")
            return

        user_prompt = prompt[1]
        reply = await ai_manager.send_request(message.from_user.id, user_prompt, category)
        await message.reply(reply)

# Регистрация хэндлеров
ai_command_handler("ai", "general")
ai_command_handler("ai-finance", "finance")
ai_command_handler("ai-reminder", "reminder")
ai_command_handler("ai-group", "group")
