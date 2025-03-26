import logging
import os
from logging.handlers import RotatingFileHandler

class CustomLogger:
    _global_logger = None

    def __init__(self, name: str, log_level=logging.DEBUG, log_dir="logs"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        if CustomLogger._global_logger is None:
            global_log_handler = RotatingFileHandler(
                os.path.join(log_dir, "bot.log"), maxBytes=10 * 1024 * 1024, backupCount=3
            )
            global_log_handler.setFormatter(formatter)
            global_log_handler.setLevel(log_level)

            root_logger = logging.getLogger("GlobalLogger")
            root_logger.setLevel(log_level)
            root_logger.addHandler(global_log_handler)

            CustomLogger._global_logger = root_logger

        file_handler = RotatingFileHandler(
            os.path.join(log_dir, f"{name}.log"), maxBytes=5 * 1024 * 1024, backupCount=3
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(log_level)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(log_level)

        if not self.logger.handlers:
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)
            self.logger.addHandler(CustomLogger._global_logger.handlers[0])

    def info(self, message: str):
        self.logger.info(message)
        CustomLogger._global_logger.info(message)

    def debug(self, message: str):
        self.logger.debug(message)
        CustomLogger._global_logger.debug(message)

    def warning(self, message: str):
        self.logger.warning(message)
        CustomLogger._global_logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)
        CustomLogger._global_logger.error(message)

    def critical(self, message: str):
        self.logger.critical(message)
        CustomLogger._global_logger.critical(message)
