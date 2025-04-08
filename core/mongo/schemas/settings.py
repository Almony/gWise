from pydantic import BaseModel


class SettingsSchema(BaseModel):
    """
    SettingsSchema defines the structure and validation rules for a specific MongoDB document.
    """

    key: str
    value: dict
