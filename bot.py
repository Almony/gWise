# gWise/bot.py

import asyncio
from core.system.bot_context import BotContext
from core.system.event_router import register_all

async def main():
    print("Loading environment and initializing context...")
    BotContext.init()

    app = BotContext.bot

    # Регистрируем все обработчики событий
    register_all(app)

    async with app:
        print("gWise bot is running...")
        await asyncio.Event().wait()  # Держим процесс активным

if __name__ == "__main__":
    asyncio.run(main())
