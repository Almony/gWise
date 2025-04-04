from core.mongo.mongo_manager import MongoManager
from core.mongo.schemas import MongoCollections

class DebugMongo:
    def __init__(self):
        self.mongo = MongoManager()

    async def get_all_collections(self):
        return list(MongoCollections.__dict__.values())

    async def get_users(self, limit=5, filter_: dict = None):
        return await self._get(MongoCollections.USERS, limit, filter_)

    async def get_reminders(self, limit=5, filter_: dict = None):
        return await self._get(MongoCollections.REMINDERS, limit, filter_)

    async def get_ai_requests(self, limit=5, filter_: dict = None):
        return await self._get(MongoCollections.AI_REQUESTS, limit, filter_)

    async def get_groups(self, limit=5, filter_: dict = None):
        return await self._get(MongoCollections.GROUPS, limit, filter_)

    async def get_group_members(self, group_id: int, limit=5):
        return await self._get(MongoCollections.GROUP_MEMBERS, limit, {"group_id": group_id})

    async def get_group_posts(self, group_id: int, limit=5):
        return await self._get(MongoCollections.GROUP_POSTS, limit, {"group_id": group_id})

    async def _get(self, collection_name, limit=5, filter_: dict = None):
        collection = self.mongo.get_collection(collection_name)
        cursor = collection.find(filter_ or {}).sort("_id", -1).limit(limit)
        return await cursor.to_list(length=limit)


# # Пример использования
# async def main():
#     dbg = DebugMongo()

#     print("🧪 Пользователи:")
#     users = await dbg.get_users(limit=3)
#     pprint(users)

#     print("\n🤖 AI-запросы:")
#     ai = await dbg.get_ai_requests(limit=2)
#     pprint(ai)

#     print("\n📦 Все коллекции:")
#     collections = await dbg.get_all_collections()
#     pprint(collections)

# if __name__ == "__main__":
#     asyncio.run(main())
