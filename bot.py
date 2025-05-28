# gWise/bot.py

import asyncio
from core.system.bot_context import BotContext
from core.system.event_router import register_all

async def main():
    BotContext.init()
    await BotContext.async_init()

    app = BotContext.bot
    logger = BotContext.logger

    logger.info("Registering event handlers...")
    register_all(app)

    async with app:
        logger.info("gWise bot is running...")
        await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
