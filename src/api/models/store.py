from models.common import DBBaseModel
from models.product import Product
from main import db


class Store(DBBaseModel):
    name: str
    description: str = ""
    active: bool = True
    products: list[Product] = []

    # def get_products(self) -> list:
    #     self.products = db.products.find({'store_id': self.id})

