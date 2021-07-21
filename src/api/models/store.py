from models.common import DBBaseModel, random_string_generator
from db import get_db
from typing import Optional
from pydantic import Field
from models.product import Product

db = get_db()


class Store(DBBaseModel):
    store_id: str = Field(
        hidden_from_schema=True,
        title="Store ID",
        default_factory=random_string_generator,
    )
    name: str
    description: Optional[str] = ""
    active: Optional[bool] = True
    products: list[Product] = Field(hidden_from_schema=True, default_factory=list)

    def get_products(self) -> list:
        """function which returns the products in the store"""
        products = db.products.find({"store_id": self.store_id})
        p = []
        for product in products:
            p.append(Product(**product))
        self.products = p
