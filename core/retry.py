import asyncio
import logging
from functools import wraps

import openai
from pyrogram.errors import FloodWait, RPCError

logger = logging.getLogger(__name__)


def retry_openai(max_attempts: int = 3, base_delay: float = 1.0):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return await func(*args, **kwargs)

                except (openai.RateLimitError, openai.APIConnectionError, openai.Timeout) as e:
                    if attempt == max_attempts:
                        logger.error(f"[OpenAI Retry] Попытка {attempt}/{max_attempts} провалилась. Ошибка: {e}")
                        raise
                    delay = base_delay * 2 ** (attempt - 1)
                    logger.warning(f"[OpenAI Retry] Ошибка: {e} | Повтор через {delay:.1f} сек...")
                    await asyncio.sleep(delay)

        return wrapper
    return decorator


def retry_telegram(max_attempts: int = 2, delay: float = 1.0):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return await func(*args, **kwargs)

                except FloodWait as e:
                    logger.warning(f"[Telegram Retry] FloodWait: ждём {e.value} сек")
                    await asyncio.sleep(e.value)
                    return await func(*args, **kwargs)

                except RPCError as e:
                    if attempt == max_attempts:
                        logger.error(f"[Telegram Retry] Попытка {attempt}/{max_attempts} провалилась. Ошибка: {e}")
                        raise
                    logger.warning(f"[Telegram Retry] Ошибка: {e} | Повтор через {delay:.1f} сек...")
                    await asyncio.sleep(delay)

        return wrapper
    return decorator
