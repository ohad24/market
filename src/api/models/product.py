from models.common import DBBaseModel
from typing import Optional


class Product(DBBaseModel):
    name: str
    description: Optional[str] = ""
    price: float = 0.0
    active: bool = True
