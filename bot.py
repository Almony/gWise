import asyncio
import argparse
import sys

if sys.platform.startswith("linux"):
    import uvloop
    uvloop.install()

from ptpython.repl import embed

from core.system.bot_context import BotContext
from core.system.event_router import register_all


async def start_bot():
    app = BotContext.bot
    logger = BotContext.logger

    logger.info("Registering event handlers...")
    register_all(app)

    async with app:
        logger.info("gWise bot is running...")
        await asyncio.Event().wait()


async def start_console():
    context = {
        "app": BotContext.bot,
        "db": BotContext.db,
    }
    banner = """
    Wllcome to interactive Bot's debug console.
    Loaded objects: app, db
    """

    print(banner)

    await embed(globals=context)


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--console", action="store_true", help="Open async console after bot start")
    args = parser.parse_args()

    BotContext.init()
    await BotContext.async_init()

    if args.console:
        await start_console()
    else:
        await start_bot()


if __name__ == "__main__":
    asyncio.run(main())
