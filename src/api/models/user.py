from models.common import DBBaseModel, random_string_generator
from typing import Optional, Any
from pydantic import Field, PrivateAttr
from main import settings


class User(DBBaseModel):
    user_id: str = Field(
        hidden_from_schema=True,
        title="User ID",
        default_factory=random_string_generator,
        min_length=settings.app_entity_id_length,
        max_length=settings.app_entity_id_length,
    )
    name: str = Field(title="User name", min_length=5, max_length=20)
    _password: Optional[str] = PrivateAttr(Field("", title="Password"))
