from core.mongo.mongo_manager import MongoManager
from core.mongo.mongo_manager import MongoCollections
from core.mongo.schemas import SettingsSchema


class SettingsManager:
    def __init__(self):
        self.mongo = MongoManager()

    async def get_setting(self, key: str) -> dict:
        settings = self.mongo.get_collection(MongoCollections.SETTINGS)
        doc = await settings.find_one({"key": key})
        return doc["value"] if doc else {}

    async def set_setting(self, key: str, value: dict):
        settings = self.mongo.get_collection(MongoCollections.SETTINGS)
        await settings.update_one({"key": key}, {"$set": {"value": value}}, upsert=True)
