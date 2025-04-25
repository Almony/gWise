import logging

LOG_LEVEL = logging.DEBUG  # Можно потом переопределить через .env, если потребуется

def setup_basic_logging():
    logging.basicConfig(
        level=LOG_LEVEL,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )
