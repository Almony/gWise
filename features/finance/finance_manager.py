# features/finance/manager.py

from core.mongo.mongo_manager import MongoManager
from core.mongo.schemas import MongoCollections
from core.logger import CustomLogger
from datetime import datetime
from core.mongo.schemas import FinanceEntrySchema

logger = CustomLogger("FinanceManager")


class FinanceManager:
    def __init__(self):
        self.mongo = MongoManager()

    async def add_transaction(
        self,
        user_id: int,
        amount: float,
        category_main: str,
        category_group: str,
        description: str = "",
        category_sub: str = None,
        is_recurring: bool = False,
        interval: str = None
    ):
        finance = self.mongo.get_collection(MongoCollections.FINANCE_ENTRIES)

        entry = FinanceEntrySchema(
            user_id=user_id,
            amount=amount,
            category={"main": category_main, "sub": category_sub},
            category_group=category_group,
            description=description,
            is_recurring=is_recurring,
            interval=interval
        )

        await finance.insert_one(entry.dict())
        logger.info(f"Транзакция от {user_id}: {amount} ({category_main})")

    async def get_user_finances(self, user_id: int, months_back: int = 3):
        finance = self.mongo.get_collection(MongoCollections.FINANCE_ENTRIES)
        from_date = datetime.utcnow().replace(day=1)  # начало месяца
        return await finance.find({
            "user_id": user_id,
            "timestamp": {"$gte": from_date}
        }).to_list(length=100)

    async def get_recurring(self, user_id: int):
        finance = self.mongo.get_collection(MongoCollections.FINANCE_ENTRIES)
        return await finance.find({
            "user_id": user_id,
            "is_recurring": True
        }).to_list(length=100)
