# gwise/core/exception_handlers.py

import asyncio
import logging
from functools import wraps

from pyrogram.types import Message, CallbackQuery
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
    async def wrapper(client, update, *args, **kwargs):
        try:
            return await func(client, update, *args, **kwargs)

        except BusinessError as e:
            await _reply(update, e.message)

        # === Telegram ===
        except FloodWait as e:
            logger.warning(f"FloodWait: ждём {e.value} сек")
            await asyncio.sleep(e.value)
            return await func(client, update, *args, **kwargs)

        except RPCError as e:
            logger.exception("Telegram API ошибка")
            await _reply(update, "Ошибка: Telegram недоступен. Попробуйте позже.")

        # === OpenAI ===
        except (openai.RateLimitError, openai.APIConnectionError, openai.Timeout) as e:
            logger.warning(f"OpenAI временная ошибка: {e}")
            raise GPTServiceUnavailable()

        except (openai.BadRequestError, openai.AuthenticationError) as e:
            logger.error(f"OpenAI ошибка запроса или авторизации: {e}")
            raise GPTBadRequest()

        except openai.OpenAIError as e:
            logger.exception("Неизвестная ошибка OpenAI")
            raise GPTServiceUnavailable()

        # === MongoDB ===
        except DuplicateKeyError:
            logger.warning("Попытка создать дублирующий документ в MongoDB")

        except PyMongoError as e:
            logger.exception("Ошибка MongoDB")
            await _reply(update, "Ошибка: не удалось обратиться к базе данных.")

        # === System ===
        except Exception as e:
            logger.exception("Непредвиденная ошибка")
            await _reply(update, "Что-то пошло не так. Мы уже работаем над этим.")

    return wrapper


async def _reply(update, text: str):
    if isinstance(update, Message):
        await update.reply_text(text)
    elif isinstance(update, CallbackQuery):
        await update.answer(text, show_alert=True)
