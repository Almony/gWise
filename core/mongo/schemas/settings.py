from pydantic import BaseModel


class SettingsSchema(BaseModel):
    key: str
    value: dict
