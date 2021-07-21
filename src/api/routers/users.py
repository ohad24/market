from models.user import User
from fastapi import APIRouter
from db import get_db

db = get_db()
router = APIRouter()


@router.get("/")
async def list_users():
    users = []
    for user in db.users.find():
        users.append(User(**user))
    return {"users": users}


@router.post("/")
async def create_user(user: User):
    ret = db.users.insert_one(user.dict(by_alias=True))
    user._db_id = ret.inserted_id
    return {"user": user}
