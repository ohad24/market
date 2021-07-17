import pymongo
import os
from main import settings


def get_db():
    db_name = settings.db_name
    db_client: pymongo.MongoClient = pymongo.MongoClient(
        host=settings.db_host,
        port=27017,
        username=settings.db_username,
        password=settings.db_password,
    )
    return db_client[db_name]
