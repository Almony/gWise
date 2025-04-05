# gwise/core/exception_handlers.py

import asyncio
import logging
from functools import wraps

from pyrogram.errors import FloodWait, RPCError
from pymongo.errors import DuplicateKeyError, PyMongoError

import openai
from exceptions import (
    BusinessError,
    GPTServiceUnavailable,
    GPTBadRequest,
)

logger = logging.getLogger(__name__)

def handle_exceptions(func):
    @wraps(func)
    async def wrapper(client, message, *args, **kwargs):
        try:
            return await func(client, message, *args, **kwargs)

        except BusinessError as e:
            await message.reply_text(e.message)

        # === Telegram ===
        except FloodWait as e:
            logger.warning(f"FloodWait: ждём {e.value} сек")
            await asyncio.sleep(e.value)
            return await func(client, message, *args, **kwargs)

        except RPCError as e:
            logger.exception("Telegram API ошибка")
            await message.reply_text("Ошибка: Telegram недоступен. Попробуйте позже.")

        # === OpenAI ===
        except openai.RateLimitError as e:
            logger.warning(f"OpenAI RateLimitError: {e}")
            raise GPTServiceUnavailable()

        except openai.APIConnectionError as e:
            logger.warning(f"OpenAI APIConnectionError: {e}")
            raise GPTServiceUnavailable()

        except openai.Timeout as e:
            logger.warning(f"OpenAI Timeout: {e}")
            raise GPTServiceUnavailable()

        except openai.BadRequestError as e:
            logger.error(f"OpenAI BadRequestError: {e}")
            raise GPTBadRequest()

        except openai.AuthenticationError as e:
            logger.error(f"OpenAI AuthenticationError: {e}")
            raise GPTBadRequest()

        except openai.OpenAIError as e:
            logger.exception("Неизвестная ошибка OpenAI")
            raise GPTServiceUnavailable()

        # === MongoDB ===
        except DuplicateKeyError:
            logger.warning("Попытка создать дублирующий документ в MongoDB")

        except PyMongoError as e:
            logger.exception("Ошибка MongoDB")
            await message.reply_text("Ошибка: не удалось обратиться к базе данных.")

        # === System ===
        except Exception as e:
            logger.exception("Непредвиденная ошибка")
            await message.reply_text("Что-то пошло не так. Мы уже работаем над этим.")

    return wrapper
