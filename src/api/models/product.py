from models.common import DBBaseModel, random_string_generator
from pydantic import condecimal
from pydantic import Field
from bson.decimal128 import Decimal128


class Product(DBBaseModel):
    product_id: str = Field(
        hidden_from_schema=True,
        title="Product ID",
        default_factory=random_string_generator,
    )
    name: str
    description: str = ""
    price: condecimal(max_digits=10, decimal_places=2) = 0.0
    active: bool = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.price = Decimal128(str(self.price))

    class Config:
        json_encoders = {Decimal128: lambda v: str(v)}
