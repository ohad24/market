from models.common import DBBaseModel, random_string_generator
from typing import Optional, Any
from pydantic import Field, PrivateAttr


class User(DBBaseModel):
    user_id: Optional[str] = Field(
        hidden_from_schema=True,
        title="User ID",
        default_factory=random_string_generator,
    )
    name: str
    _password: Optional[str] = PrivateAttr(Field("", title="Password"))
