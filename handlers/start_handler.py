# gWise/handlers/start_handler.py

from pyrogram import Client, filters

def register(app: Client):
    @app.on_message(filters.command("start"))
    async def start_handler(client, message):
        await message.reply("Привет! Я gWise бот 🚀")
