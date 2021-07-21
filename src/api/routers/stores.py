from models.store import Store
from fastapi import APIRouter
from db import get_db
from config import apihttpexception

db = get_db()
router = APIRouter()


@router.get("/")
async def list_stores():
    stores = []
    for store in db.stores.find():
        stores.append(Store(**store).dict(exclude={"products"}))
    return {"stores": stores}


@router.post("/")
async def create_store(store: Store):
    ret = db.stores.insert_one(store.dict(by_alias=True))
    store._db_id = ret.inserted_id
    return {"store": store.dict(exclude={"products"})}


@router.get("/{store_id}")
async def read_store(store_id):
    ret = db.stores.find_one({"store_id": store_id})
    if not ret:
        raise apihttpexception.store.e404
    return {"store": Store(**ret)}


@router.get("/{store_id}/products")
async def list_products_in_store(store_id):
    ret = db.stores.find_one({"store_id": store_id})
    if not ret:
        raise apihttpexception.store.e404
    store = Store(**ret)
    store.get_products()
    return {"store": store}
