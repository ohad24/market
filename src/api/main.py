from logging import debug
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import pymongo
from models.user import User
import uvicorn

client = pymongo.MongoClient(
    host="localhost", port=27017, username="root", password="example"
)
db = client.test

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users")
async def list_users():
    users = []
    for user in db.users.find():
        # print(user)
        users.append(User(**user))
    return {"users": users}


@app.post("/users")
async def create_user(user: User):
    if hasattr(user, "id"):
        delattr(user, "id")
    ret = db.users.insert_one(user.dict(by_alias=True))
    user.id = ret.inserted_id
    return {"user": user}


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True, access_log=True, debug=True)
