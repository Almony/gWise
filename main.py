from pyrogram import Client
from core.config import settings
from core.logger import CustomLogger

logger = CustomLogger("Main")

app = Client(
    name="my_bot",
    api_id=settings.API_ID,
    api_hash=settings.API_HASH,
    bot_token=settings.BOT_TOKEN
)

@app.on_message()
async def fallback_handler(_, message):
    await message.reply("Привет! Я пока только учусь 😊")

if __name__ == "__main__":
    logger.info("Запуск бота...")
    app.run()
