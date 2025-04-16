import pytest
from features.ai.manager import ai_manager

@pytest.mark.asyncio
async def test_ai_request():
    response = await ai_manager.send_request(123456789, "Привет, кто ты?", "general")
    assert isinstance(response, str)
