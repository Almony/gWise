# gWise/handlers/gpt_handler.py

from pyrogram import Client, filters

def register(app: Client):
    @app.on_message(filters.command(["analyze", "stats"]))
    async def gpt_handler(client, message):
        await message.reply("Функция AI-анализа скоро будет доступна! 🔥")
