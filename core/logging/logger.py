import logging
from core.logging.logging_config import LOGGING_CONFIG  # ensures config is applied

def get_logger(name: str) -> logging.Logger:
    """
    Возвращает логгер с заданным именем, уже настроенный по конфигурации.
    Используется во всех модулях проекта gWise.
    """
    return logging.getLogger(name)
