import pytest
from features.reminder_manager import reminder_manager
from datetime import datetime, timedelta

@pytest.mark.asyncio
async def test_add_reminder():
    due = datetime.utcnow() + timedelta(minutes=1)
    await reminder_manager.add_reminder(123456789, "позвонить маме", due)
