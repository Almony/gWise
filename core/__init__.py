from .system.config import settings
from .logging.logger import CustomLogger
from .system.event_router import (
    event_router,
    on_message,
    on_callback_query,
    on_edited_message,
    register_all
)
