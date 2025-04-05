# gwise/logging/telegram_reporter.py

import logging
# import os
import traceback
import html
import requests
from core.system import Settings

TG_API_URL = f"https://api.telegram.org/bot{Settings.BOT_TOKEN}/sendMessage"


class TelegramErrorHandler(logging.Handler):
    def __init__(self, level=logging.ERROR):
        super().__init__(level)

    def emit(self, record):
        if not Settings.BOT_TOKEN or not Settings.ADMIN_LOG_CHAT_ID:
            return  # не настроено

        try:
            log_entry = self.format(record)
            message = html.escape(log_entry)

            payload = {
                "chat_id": Settings.ADMIN_LOG_CHAT_ID,
                "text": f"🚨 <b>Ошибка</b>:\n<pre>{message}</pre>",
                "parse_mode": "HTML",
                "disable_web_page_preview": True,
            }

            requests.post(TG_API_URL, data=payload, timeout=5)
        except Exception:
            self.handleError(record)
