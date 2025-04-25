import asyncio
import logging
import openai

from functools import wraps
from typing import Callable, Awaitable, Union

from core.system.bot_context import BotContext
from core.logging.telegram_reporter import report_error_to_telegram
from exceptions.business_exceptions import BusinessException, GPTServiceUnavailable, GPTBadRequest
from pyrogram.types import Message, CallbackQuery
from pyrogram.errors import FloodWait, RPCError
from pymongo.errors import DuplicateKeyError, PyMongoError

logger = BotContext.logger

def handle_exceptions(func: Callable[..., Awaitable]) -> Callable[..., Awaitable]:
    """
    Декоратор для централизованной обработки всех исключений в хендлерах.
    """

    @wraps(func)
    async def wrapper(client, update: Union[Message, CallbackQuery], *args, **kwargs):
        try:
            return await func(client, update, *args, **kwargs)

        except BusinessException as e:
            await _reply(update, e.message)
            return

        # === Telegram ===
        except FloodWait as e:
            logger.warning(f"FloodWait: ждём {e.value} секунд.")
            await asyncio.sleep(e.value)
            return await func(client, update, *args, **kwargs)

        except RPCError as e:
            logger.exception("Telegram API ошибка.")
            await _reply(update, "Ошибка: Telegram временно недоступен. Попробуйте позже.")
            return

        # === OpenAI ===
        except (openai.RateLimitError, openai.APIConnectionError, openai.Timeout) as e:
            logger.warning(f"OpenAI временная ошибка: {e}")
            raise GPTServiceUnavailable()

        except (openai.BadRequestError, openai.AuthenticationError) as e:
            logger.error(f"OpenAI ошибка запроса или авторизации: {e}")
            raise GPTBadRequest()

        except openai.OpenAIError as e:
            logger.exception("Неизвестная ошибка OpenAI.")
            raise GPTServiceUnavailable()

        # === MongoDB ===
        except DuplicateKeyError:
            logger.warning("Попытка создать дублирующий документ в MongoDB.")
            return

        except PyMongoError as e:
            logger.exception("Ошибка MongoDB.")
            await _reply(update, "Ошибка: проблемы с базой данных. Попробуйте позже.")
            return

        # === System (любые другие ошибки) ===
        except Exception as e:
            logger.exception("Непредвидённая ошибка.")
            await _reply(update, "Что-то пошло не так. Мы уже работаем над этим.")
            await report_error_to_telegram(repr(e))
            return

    return wrapper

async def _reply(update: Union[Message, CallbackQuery], text: str):
    """
    Отвечает пользователю или показывает alert в зависимости от типа объекта.
    """
    try:
        if isinstance(update, Message):
            await update.reply_text(text)
        elif isinstance(update, CallbackQuery):
            await update.answer(text, show_alert=True)
    except Exception as e:
        logger.warning(f"Ошибка при попытке отправить ответ: {e}")
