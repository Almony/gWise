from core.base import BaseManager
from core.mongo.schemas import MongoCollections, AIRequestSchema

class AIHistoryManager(BaseManager):
    def __init__(self):
        super().__init__("AIHistory")

    async def log_ai_request(self, schema: AIRequestSchema):
        collection = self.get_collection(MongoCollections.AI_REQUESTS)
        await collection.insert_one(schema.dict())
        self.logger.debug(f"Сохранён AI-запрос от {schema.user_id}")
