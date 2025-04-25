# gWise/handlers/subscription_handler.py

from pyrogram import Client, filters

def register(app: Client):
    @app.on_message(filters.command("myplan"))
    async def myplan_handler(client, message):
        await message.reply("Ваша текущая подписка: Free 🚀")
