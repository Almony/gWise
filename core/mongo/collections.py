from enum import Enum


class MongoCollections(Enum):

    USERS = "users"
    REMINDERS = "reminders"
    REMINDERS_ARCHIVE = "reminders_archive"
    FINANCE_ENTRIES = "finance_entries"
    AI_REQUESTS = "ai_requests"
    GROUPS = "groups"
    GROUP_MEMBERS = "group_members"
    GROUP_POSTS = "group_posts"
    CHANNELS = "channels"
    CHANNEL_POSTS = "channel_posts"
    CHATS = "chats"
    CHAT_MEMBERS = "chat_members"
    CHAT_POSTS = "chat_posts"
    SETTINGS = "settings"
    LOGS_SYSTEM = "logs_system"
