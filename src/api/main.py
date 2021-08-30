from fastapi import FastAPI, Depends
from fastapi import APIRouter, HTTPException, status
from base_common import get_settings, Settings, User
from routers import users, stores, products
from auth import (
    get_current_active_user,
    OAuth2PasswordRequestForm,
    authenticate_user,
    Token,
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
from datetime import timedelta


app = FastAPI()
app.include_router(APIRouter())
base_router = APIRouter(prefix="/api/v1")
base_router.include_router(users.router, prefix="/users")
base_router.include_router(stores.router, prefix="/stores")
base_router.include_router(products.router, prefix="/products")


@app.get("/")
@base_router.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/info")
async def info(
    settings: Settings = Depends(get_settings),
    current_user: User = Depends(
        get_current_active_user
    ),  # TODO: REMOVE AUTH FROM ROUTE AND FROM TEST,
):
    return settings


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:  # ! TEST THIS
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.name}, expires_delta=access_token_expires
    )
    print("login_for_access_token")
    return {"access_token": access_token, "token_type": "bearer"}


app.include_router(base_router)
