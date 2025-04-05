from pyrogram import Client, filters
from pyrogram.types import Message
from features.ai import ai_manager
from features.subscription import check_tokens
from core import on_message, CustomLogger
from core.handlers import handle_exceptions



logger = CustomLogger("ai_handler")


def ai_command_handler(command_name: str, category: str):
    @on_message(filters.command(command_name))
    @check_tokens()
    @handle_exceptions
    async def handler(client: Client, message: Message):
        prompt = message.text.split(maxsplit=1)
        if len(prompt) < 2:
            await message.reply("✍️ Пожалуйста, добавь текст запроса после команды.")
            return

        user_prompt = prompt[1]
        reply = await ai_manager.send_request(message.from_user.id, user_prompt, category)
        await message.reply(reply)

ai_command_handler("ai", "general")
ai_command_handler("ai-finance", "finance")
ai_command_handler("ai-reminder", "reminder")
ai_command_handler("ai-group", "group")
