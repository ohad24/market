from fastapi import FastAPI, Depends
from fastapi import APIRouter
from config import Settings, get_settings
from routers import users


app = FastAPI()
app.include_router(APIRouter())
base_router = APIRouter(prefix="/api/v1")
base_router.include_router(users.router, prefix="/users")


@app.get("/")
@base_router.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/info")
async def info(settings: Settings = Depends(get_settings)):
    return settings


app.include_router(base_router)
