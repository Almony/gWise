import pytest
from features.subscription.manager import subscription_manager

@pytest.mark.asyncio
async def test_subscription_logic():
    user_id = 123456789
    sub = await subscription_manager.get_subscription(user_id)
    assert sub["type"] == "free"
    assert sub["ai_requests_left"] >= 0

    available = await subscription_manager.has_available_requests(user_id)
    assert isinstance(available, bool)

    if available:
        await subscription_manager.decrement_request(user_id)
