import pytest
from core.mongo_manager import MongoManager

@pytest.mark.asyncio
async def test_create_user():
    mongo = MongoManager()
    user_id = 123456789
    user = await mongo.create_user(user_id, "Test", "testuser")
    assert user["user_id"] == user_id
    assert user["subscription"]["type"] == "free"
