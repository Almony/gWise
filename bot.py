import sys
import asyncio
import argparse

if sys.platform.startswith("linux"):
    import uvloop
    uvloop.install()

from core.system.bot_context import BotContext
from core.system.event_router import register_all


async def start_bot():
    BotContext.init()
    await BotContext.async_init()

    app = BotContext.bot
    logger = BotContext.logger

    logger.info("Registering event handlers...")
    register_all(app)

    async with app:
        logger.info("gWise bot is running...")
        await asyncio.Event().wait()


async def open_console():
    from aioconsole import start_interactive_server

    banner = "Async gWise Console — `ctx`, `db`, `bot`, `logger`"
    print(banner)
    locals={
            "bot": BotContext.bot,
            "db": BotContext.db,
            "logger": BotContext.logger,
            "ctx": BotContext,
        }

    server = await start_interactive_server(host="localhost", port=4444)
    await server.wait_closed()

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--console", action="store_true", help="Open async console after bot start")
    args = parser.parse_args()

    if args.console:
        tasks = [asyncio.create_task(open_console())]
    else:
        tasks = [asyncio.create_task(start_bot())]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
