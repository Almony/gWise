from core.mongo.mongo_manager import MongoManager
from core.mongo.schemas import MongoCollections, SystemLogSchema
from core.logger import CustomLogger

logger = CustomLogger("SystemLogger")


class SystemLoggerDB:
    def __init__(self):
        self.mongo = MongoManager()

    async def log_event(self, level: str, event_type: str, message: str, context: dict = None):
        collection = self.mongo.get_collection(MongoCollections.LOGS_SYSTEM)
        log_entry = SystemLogSchema(
            level=level,
            event_type=event_type,
            message=message,
            context=context or {}
        )
        await collection.insert_one(log_entry.dict())
        logger.debug(f"[DB_LOG] {level} - {event_type} - {message}")
