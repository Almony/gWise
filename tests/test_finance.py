import pytest
from features.finance_manager import finance_manager

@pytest.mark.asyncio
async def test_add_transaction():
    await finance_manager.add_transaction(123456789, 99.99, "food", "пицца")
