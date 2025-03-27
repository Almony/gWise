from core.mongo_manager import MongoManager
from core.logger import CustomLogger
from datetime import datetime

logger = CustomLogger("ReminderManager")

class ReminderManager:
    def __init__(self):
        self.mongo = MongoManager()

    async def add_reminder(self, user_id: int, text: str, due_time: datetime):
        reminders = self.mongo.get_collection("reminders")
        doc = {
            "user_id": user_id,
            "text": text,
            "due_time": due_time,
            "notified": False
        }
        await reminders.insert_one(doc)
        logger.info(f"Добавлено напоминание для {user_id}: {text}")

    async def get_due_reminders(self):
        now = datetime.utcnow()
        reminders = self.mongo.get_collection("reminders")
        return await reminders.find({"due_time": {"$lte": now}, "notified": False}).to_list(length=100)

    async def mark_notified(self, reminder_id):
        reminders = self.mongo.get_collection("reminders")
        await reminders.update_one({"_id": reminder_id}, {"$set": {"notified": True}})


reminder_manager = ReminderManager()
