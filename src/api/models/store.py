from models.common import DBBaseModel, random_string_generator
from db import get_db
from typing import Optional
from pydantic import Field

db = get_db()


class Store(DBBaseModel):
    store_id: str = Field(
        hidden_from_schema=True,
        title="Store ID",
        default_factory=random_string_generator,
    )
    name: str
    description: str = ""
    active: bool = True
    # products: list[Product] = []

    def get_products(self) -> list:
        """ function which returns the products in the store """
        self.products = db.products.find({'store_id': self.id})
        return self.products

