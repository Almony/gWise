from core.mongo.client import db
from core.logging.logger import CustomLogger
from core.mongo.schemas import MongoCollections

logger = CustomLogger("MongoBase")


def get_collection(name: str):
    """
    get_collection is a function used to perform a specific task within the module.
    """

    if not hasattr(MongoCollections, name.upper()):
        logger.warning(f"Запрос к несуществующей коллекции: {name}")
    collection = db[name]
    logger.debug(f"Получена коллекция: {name}")
    return collection
