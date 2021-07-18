from models.common import DBBaseModel
from typing import Optional, Any
from pydantic import Field, PrivateAttr
import random
import string


class User(DBBaseModel):
    user_id: Optional[str] = Field(hidden_from_schema=True, title="User ID")
    name: str
    _password: Optional[str] = PrivateAttr(Field("", title="Password"))

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        self.user_id = "".join(
            random.choices(string.ascii_lowercase + string.digits, k=10)
        )
