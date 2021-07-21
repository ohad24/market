from models.product import Product
from fastapi import APIRouter
from db import get_db

db = get_db()
router = APIRouter()


@router.get("/")
async def list_products():
    products = []
    for product in db.products.find():
        products.append(Product(**product))
    return {"products": products}


@router.post("/")
async def create_product(product: Product):
    ret = db.products.insert_one(product.dict(by_alias=True))
    product._db_id = ret.inserted_id
    return {"product": product}
