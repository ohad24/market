from models.common import DBBaseModel, random_string_generator
from db import get_db
from typing import Optional
from pydantic import Field
from models.product import Product
from base_common import settings

db = get_db()


class Store(DBBaseModel):
    store_id: str = Field(
        hidden_from_schema=True,
        title="Store ID",
        default_factory=random_string_generator,
        min_length=settings.app_entity_id_length,
        max_length=settings.app_entity_id_length,
    )
    name: str = Field(title="Store name", min_length=2, max_length=50)
    description: Optional[str] = Field(
        title="Store description", default=None, max_length=500
    )
    active: Optional[bool] = Field(title="Is store active", default=True)
    products: list[Product] = Field(
        hidden_from_schema=True, default_factory=list, title="Products in store"
    )

    class Config:
        title = "Store model"

    def get_products(self) -> list:
        """function which returns the products in the store"""
        products = db.products.find({"store_id": self.store_id})
        p = []
        for product in products:
            p.append(Product(**product))
        self.products = p
