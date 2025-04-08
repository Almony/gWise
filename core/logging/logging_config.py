import logging
from core.logging.telegram_reporter import TelegramErrorHandler


def setup_logging():
    """
    setup_logging configures and initializes the logging system.
    """

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    logger.addHandler(console)

    tg_handler = TelegramErrorHandler()
    tg_handler.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s\n%(exc_text)s')
    tg_handler.setFormatter(formatter)
    logger.addHandler(tg_handler)
