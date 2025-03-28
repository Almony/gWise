from pyrogram import Client, filters
from core.config import settings
from core.logger import CustomLogger

from handlers.help import help_handler
from handlers.ai import ai_handler
from handlers.start import start_handler


logger = CustomLogger("Main")


app = Client(
    name="gWise",
    api_id=settings.API_ID,
    api_hash=settings.API_HASH,
    bot_token=settings.BOT_TOKEN
)

@app.on_message(filters.text & ~filters.command(["start", "help", "ai", "ai-finance", "ai-reminder", "ai-group"]))
async def fallback_handler(_, message):
    await message.reply("Привет! Я пока только учусь 😊")

if __name__ == "__main__":
    logger.info("Запуск бота...")
    app.run()
