from typing import Optional
from models.common import DBBaseModel, random_string_generator
from pydantic import Field, validator, condecimal
from bson.decimal128 import Decimal128
from db import get_db
from base_common import settings

db = get_db()


class Product(DBBaseModel):
    product_id: str = Field(
        hidden_from_schema=True,
        title="Product ID",
        default_factory=random_string_generator,
        min_length=settings.app_entity_id_length,
        max_length=settings.app_entity_id_length,
    )
    name: str = Field(title="Product name", min_length=3, max_length=200)
    description: Optional[str] = Field(
        title="Product description", max_length=500, default=None
    )
    price: condecimal(max_digits=8, decimal_places=2) = Field(
        title="Product price",
        min_value="0.00",
        max_value="999999.99",
        default="0.00",
    )
    active: bool = Field(title="Is product active", default=True)
    store_id: str = Field(title="Store ID", default="")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.price = Decimal128(str(self.price))

    @validator("store_id")
    def check_store_id(cls, v):
        ret = db.stores.find_one({"store_id": v})
        if not ret:
            raise ValueError("Store ID not found")
        return v
