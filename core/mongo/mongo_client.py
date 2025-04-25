# gWise/core/mongo/mongo_client.py

from typing import Any, Dict, List, Optional
from motor.motor_asyncio import AsyncIOMotorDatabase
from pymongo import ReturnDocument

class MongoClientWrapper:
    def __init__(self, db: AsyncIOMotorDatabase): # type: ignore
        self.db = db

    async def insert_one(self, collection: str, document: dict) -> Any:
        result = await self.db[collection].insert_one(document)
        return result.inserted_id

    async def find_one(self, collection: str, query: dict) -> Optional[dict]:
        document = await self.db[collection].find_one(query)
        return document

    async def find_many(self, collection: str, query: dict) -> List[dict]:
        cursor = self.db[collection].find(query)
        return await cursor.to_list(length=None)

    async def update_one(self, collection: str, query: dict, update: dict, upsert: bool = False) -> Optional[dict]:
        result = await self.db[collection].find_one_and_update(
            query,
            {"$set": update},
            upsert=upsert,
            return_document=ReturnDocument.AFTER
        )
        return result

    async def delete_one(self, collection: str, query: dict) -> Any:
        result = await self.db[collection].delete_one(query)
        return result.deleted_count
