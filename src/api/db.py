import pymongo
from base_common import settings


def get_db_client():
    return pymongo.MongoClient(
        host=settings.db_host,
        port=27017,
        username=settings.db_username,
        password=settings.db_password,
    )

def get_db():
    db_name = settings.db_name
    # print(f"db_name: {db_name}")
    db_client = get_db_client()
    return db_client[db_name]
