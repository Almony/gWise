from core.logger import CustomLogger
from core.mongo import get_collection


class BaseManager:
    def __init__(self, name: str):
        self.logger = CustomLogger(name)
        self.get_collection = get_collection  # быстрый доступ к коллекциям
