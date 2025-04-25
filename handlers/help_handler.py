# gWise/handlers/help_handler.py

from pyrogram import Client, filters

def register(app: Client):
    @app.on_message(filters.command("help"))
    async def help_handler(client, message):
        await message.reply(
            "Доступные команды:\n"
            "\t/start\n")
