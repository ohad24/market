from models.common import DBBaseModel
from typing import Optional
from datetime import datetime, timezone


class User(DBBaseModel):
    name: str
    password: Optional[str]
    create_date: Optional[datetime] = datetime.now(timezone.utc)
