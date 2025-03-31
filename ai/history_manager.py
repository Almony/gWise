# features/ai/manager.py

from core.mongo.mongo_manager import MongoManager
from core.mongo.schemas import MongoCollections
from core.mongo.schemas import AIRequestSchema
from core.logger import CustomLogger

logger = CustomLogger("AIManager")


class AIHistoryManager:
    def __init__(self):
        self.mongo = MongoManager()

    async def log_ai_request(self, schema: AIRequestSchema):
        collection = self.mongo.get_collection(MongoCollections.AI_REQUESTS)
        await collection.insert_one(schema.dict())
        logger.debug(f"Сохранён AI-запрос от {schema.user_id}")
