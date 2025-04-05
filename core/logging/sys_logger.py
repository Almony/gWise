from core.base import BaseManager
from core.mongo.schemas import MongoCollections, SystemLogSchema


class SystemLoggerDB(BaseManager):
    def __init__(self):
        super().__init__("SystemLogger")

    async def log_event(self, level: str, event_type: str, message: str, context: dict = None):
        collection = self.get_collection(MongoCollections.LOGS_SYSTEM)
        log_entry = SystemLogSchema(
            level=level,
            event_type=event_type,
            message=message,
            context=context or {}
        )
        await collection.insert_one(log_entry.dict())
        self.logger.debug(f"[DB_LOG] {level} - {event_type} - {message}")
