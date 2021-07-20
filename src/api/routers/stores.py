from models.store import Store
from fastapi import APIRouter
from db import get_db

db = get_db()
router = APIRouter()


@router.get("/")
async def list_stores():
    stores = []
    for store in db.stores.find():
        stores.append(Store(**store))
    return {"stores": stores}


@router.post("/")
async def create_store(store: Store):
    if hasattr(store, "id"):
        delattr(store, "id")
    ret = db.stores.insert_one(store.dict(by_alias=True))
    store._db_id = ret.inserted_id
    return {"store": store}
