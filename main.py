from pyrogram import Client, filters
from core.system.config import settings
from core.logging.logger import CustomLogger
from core.system.event_router import register_all

from handlers import help_handler
from handlers import ai_handler
from handlers import start_handler


logger = CustomLogger("Main")


app = Client(
    name="gWise",
    api_id=settings.API_ID,
    api_hash=settings.API_HASH,
    bot_token=settings.BOT_TOKEN
)

@app.on_message(filters.text & ~filters.command(["start", "help", "ai"])) # "ai-finance", "ai-reminder", "ai-group"
async def fallback_handler(_, message):
    await message.reply("Привет! используй /help чтобы узнать о моих возможностях")

if __name__ == "__main__":
    logger.info("Запуск бота...")
    register_all(app=app)
    app.run()
