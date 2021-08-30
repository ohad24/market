from passlib.context import CryptContext
from jose import JWTError, jwt
from pydantic import BaseModel
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from base_common import db, User
from fastapi import Depends, FastAPI, HTTPException, status
from typing import Optional

# TODO: TO settings / base_common
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# TODO: MOVE TO models
class Token(BaseModel):
    access_token: str
    token_type: str


# TODO: MOVE TO models
class TokenData(BaseModel):
    username: Optional[str] = None


# TODO: MOVE TO settings / base_common
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(username: str):
    users_data = db.users.find_one({"name": username})
    if users_data and username in users_data.get("name"):
        a = User(**users_data)
        return a


def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False  # ! TEST THIS
    if not verify_password(password, user.password):
        return False  # ! TEST THIS
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)  # ! CHECK / TEST THIS
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(f"payload: {payload}")
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception  # ! TEST THIS
        token_data = TokenData(username=username)
    except JWTError:  # ! TEST THIS
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    # TODO: ADD A CHECK IF USER IS ACTIVE
    # if current_user.disabled:
    #     raise HTTPException(status_code=400, detail="Inactive user")
    return current_user