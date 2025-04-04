from .config import settings
from .logger import CustomLogger
from .event_router import (
    event_router,
    on_message,
    on_callback_query,
    on_edited_message,
    register_all
)
