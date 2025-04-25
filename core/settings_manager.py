from core.base import BaseManager
from core.mongo.schemas import MongoCollections, SettingsSchema


class SettingsManager(BaseManager):
    """
    SettingsManager provides centralized access and control over related components or services.
    """

    def __init__(self):
        super().__init__("SettingsManager")

    async def get_setting(self, key: str) -> dict:
        settings = self.get_collection(MongoCollections.SETTINGS)
        doc = await settings.find_one({"key": key})
        return doc["value"] if doc else {}

    async def set_setting(self, key: str, value: dict):
        settings = self.get_collection(MongoCollections.SETTINGS)
        await settings.update_one({"key": key}, {"$set": {"value": value}}, upsert=True)
