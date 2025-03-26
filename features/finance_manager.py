from core.mongo_manager import MongoManager
from core.logger import CustomLogger
from datetime import datetime

logger = CustomLogger("FinanceManager")

class FinanceManager:
    def __init__(self):
        self.mongo = MongoManager()

    async def add_transaction(self, user_id: int, amount: float, category: str, description: str = ""):
        finances = self.mongo.get_collection("finance")
        doc = {
            "user_id": user_id,
            "amount": amount,
            "category": category,
            "description": description,
            "timestamp": datetime.utcnow()
        }
        await finances.insert_one(doc)
        logger.info(f"Транзакция от {user_id}: {amount} ({category})")

    async def get_user_finances(self, user_id: int, months_back: int = 3):
        finances = self.mongo.get_collection("finance")
        from_date = datetime.utcnow().replace(day=1)  # упрощённо: с начала месяца
        return await finances.find({
            "user_id": user_id,
            "timestamp": {"$gte": from_date}
        }).to_list(length=100)

finance_manager = FinanceManager()
