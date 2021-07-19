from models.common import DBBaseModel
from models.product import Product
from db import get_db

db = get_db()


class Store(DBBaseModel):
    name: str
    description: str = ""
    active: bool = True
    # products: list[Product] = []

    def get_products(self) -> list:
        """ function which returns the products in the store """
        self.products = db.products.find({'store_id': self.id})
        return self.products

