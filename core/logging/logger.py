# gWise/core/logging/logger.py

import logging
from core.logging.logging_config import setup_basic_logging

class CustomLogger:
    def __init__(self, name: str):
        setup_basic_logging()
        self.logger = logging.getLogger(name)

    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)
