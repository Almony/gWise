import os
import logging
from logging.config import dictConfig
from pathlib import Path

# === Создание директории logs ===
LOG_DIR = Path(__file__).resolve().parent.parent.parent / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

# === Режим отладки из ENV ===
DEBUG = True

# === Общий формат логов ===
LOG_FORMAT = "[%(asctime)s] %(levelname)s | %(name)s | %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# === Конфигурация логов ===
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": LOG_FORMAT,
            "datefmt": DATE_FORMAT,
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "DEBUG" if DEBUG else "INFO",
        },
        "bot_file": {
            "class": "logging.FileHandler",
            "filename": str(LOG_DIR / "bot.log"),
            "formatter": "default",
            "encoding": "utf-8",
            "level": "INFO",
        },
        "ai_file": {
            "class": "logging.FileHandler",
            "filename": str(LOG_DIR / "ai.log"),
            "formatter": "default",
            "encoding": "utf-8",
            "level": "DEBUG",
        },
        "system_file": {
            "class": "logging.FileHandler",
            "filename": str(LOG_DIR / "system.log"),
            "formatter": "default",
            "encoding": "utf-8",
            "level": "WARNING",
        },
    },
    "loggers": {
        "gwise": {
            "handlers": ["bot_file", "console"],
            "level": "DEBUG" if DEBUG else "INFO",
            "propagate": False,
        },
        "gwise.ai": {
            "handlers": ["ai_file", "console"],
            "level": "DEBUG",
            "propagate": False,
        },
        "external": {
            "handlers": ["system_file"],
            "level": "WARNING",
            "propagate": False,
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}

# === Применение конфигурации ===
dictConfig(LOGGING_CONFIG)

# === Привязка сторонних логгеров к external ===
external_logger_names = [
    "httpx", "motor", "asyncio", "telegram", "urllib3"
]

for ext_name in external_logger_names:
    logging.getLogger(ext_name).parent = logging.getLogger("external")
    logging.getLogger(ext_name).propagate = True
    logging.getLogger(ext_name).setLevel(logging.WARNING)
