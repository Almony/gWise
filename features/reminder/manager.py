from datetime import datetime
from uuid import uuid4
from core.base import BaseManager
from core.mongo.schemas import MongoCollections

class ReminderManager(BaseManager):
    def __init__(self):
        super().__init__("ReminderManager")

    async def add_reminder(
        self,
        user_id: int,
        title: str,
        event_date: datetime,
        remind_at: list[datetime],
        description: str = "",
        is_recurring: bool = False,
        interval: str = None
    ):
        reminders = self.get_collection(MongoCollections.REMINDERS)
        doc = {
            "event_id": str(uuid4()),
            "user_id": user_id,
            "title": title,
            "description": description,
            "event_date": event_date,
            "remind_at": remind_at,
            "is_recurring": is_recurring,
            "interval": interval if is_recurring else None,
            "status": "active",
            "notified": False,
            "created_at": datetime.utcnow()
        }
        await reminders.insert_one(doc)
        self.logger.info(f"Новое напоминание от {user_id}: {title}")

    async def get_due_reminders(self, time_limit: datetime):
        reminders = self.get_collection(MongoCollections.REMINDERS)
        return await reminders.find({
            "remind_at": {"$elemMatch": {"$lte": time_limit}},
            "notified": False,
            "status": "active"
        }).to_list(length=100)

    async def mark_notified(self, reminder_id):
        reminders = self.get_collection(MongoCollections.REMINDERS)
        await reminders.update_one({"_id": reminder_id}, {"$set": {"notified": True}})
        self.logger.debug(f"Помечено как уведомлённое: {reminder_id}")

    async def archive_reminder(self, reminder_id):
        reminders = self.get_collection(MongoCollections.REMINDERS)
        archive = self.get_collection(MongoCollections.REMINDERS_ARCHIVE)

        reminder = await reminders.find_one({"_id": reminder_id})
        if reminder:
            reminder["archived_at"] = datetime.utcnow()
            await archive.insert_one(reminder)
            await reminders.delete_one({"_id": reminder_id})
            self.logger.info(f"Архивировано напоминание {reminder_id}")

    async def get_upcoming_reminders(self, user_id: int, limit: int = 10):
        reminders = self.get_collection(MongoCollections.REMINDERS)
        now = datetime.utcnow()
        return await reminders.find({
            "user_id": user_id,
            "event_date": {"$gte": now},
            "status": "active"
        }).sort("event_date", 1).to_list(length=limit)
