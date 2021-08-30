from base_common import User
from fastapi import APIRouter
from db import get_db
from base_common import get_password_hash

db = get_db()
router = APIRouter()


@router.get("/")
async def list_users():
    users = []
    for user in db.users.find():
        users.append(User(**user).dict(exclude={"password"}))
    return {"users": users}


@router.post("/")
async def create_user(user: User):
    # TODO: add password validation
    # TODO: add user validation - if user already exists
    user.password = get_password_hash(user.password)
    ret = db.users.insert_one(user.dict(by_alias=True))
    user._db_id = ret.inserted_id
    return {"user": user.dict(exclude={"password"})}
