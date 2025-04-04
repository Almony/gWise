import asyncio
from core.mongo.mongo_manager import MongoManager
from core.mongo.schemas import MongoCollections

async def clear_all_collections():
    mongo = MongoManager()
    collections = [
        MongoCollections.USERS,
        MongoCollections.REMINDERS,
        MongoCollections.REMINDERS_ARCHIVE,
        MongoCollections.FINANCE_ENTRIES,
        MongoCollections.AI_REQUESTS,
        MongoCollections.GROUPS,
        MongoCollections.GROUP_MEMBERS,
        MongoCollections.GROUP_POSTS,
        MongoCollections.SETTINGS,
        MongoCollections.LOGS_SYSTEM,
        MongoCollections.LOGS_USER_ACTIVITY
    ]

    for name in collections:
        col = mongo.get_collection(name)
        result = await col.delete_many({})
        print(f"🧨 {name}: удалено {result.deleted_count} документов")

# if __name__ == "__main__":
#     asyncio.run(clear_all_collections())
