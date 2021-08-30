from config import Settings, get_settings
settings = get_settings()
from models.user import User
from db import get_db
db = get_db()
from auth import get_password_hash
