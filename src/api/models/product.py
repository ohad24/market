from models.common import DBBaseModel
from typing import Optional
from pydantic import condecimal


class Product(DBBaseModel):
    name: str
    description: Optional[str] = ""
    price: condecimal(max_digits=2, decimal_places=2) = 0.0
    active: bool = True
