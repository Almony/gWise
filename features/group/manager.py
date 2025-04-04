from datetime import datetime
from core.base import BaseManager
from core.mongo.schemas import MongoCollections, GroupSchema, GroupMemberSchema, GroupPostSchema

class GroupManager(BaseManager):
    def __init__(self):
        super().__init__("GroupManager")

    async def add_group(self, group_id: int, title: str, type_: str, owner_id: int):
        groups = self.get_collection(MongoCollections.GROUPS)
        existing = await groups.find_one({"group_id": group_id})
        if existing:
            self.logger.debug(f"Группа уже существует: {group_id}")
            return
        doc = GroupSchema(
            group_id=group_id,
            title=title,
            type=type_,
            owner_id=owner_id
        )
        await groups.insert_one(doc.dict())
        self.logger.info(f"Добавлена новая группа: {title} ({group_id})")

    async def save_post(self, data: GroupPostSchema):
        posts = self.get_collection(MongoCollections.GROUP_POSTS)
        await posts.insert_one(data.dict())
        self.logger.debug(f"Пост {data.post_id} в группе {data.group_id} сохранён")

    async def add_member(self, data: GroupMemberSchema):
        members = self.get_collection(MongoCollections.GROUP_MEMBERS)
        await members.update_one(
            {"group_id": data.group_id, "user_id": data.user_id},
            {"$set": data.dict()},
            upsert=True
        )
        self.logger.debug(f"Участник {data.user_id} добавлен/обновлён в {data.group_id}")

    async def log_member_activity(self, group_id: int, user_id: int, field: str):
        members = self.get_collection(MongoCollections.GROUP_MEMBERS)
        await members.update_one(
            {"group_id": group_id, "user_id": user_id},
            {"$set": {f"last_{field}_at": datetime.utcnow()}}
        )
        self.logger.debug(f"{field} зафиксировано у {user_id} в {group_id}")
