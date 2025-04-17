# Utility functions for channel analyzer module

from datetime import datetime, timezone

def get_current_utc_timestamp() -> datetime:
    """Returns the current UTC timestamp."""
    return datetime.now(timezone.utc)
