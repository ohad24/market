import pymongo
import os


db_client: pymongo.MongoClient = pymongo.MongoClient(
    host="localhost", port=27017, username="root", password="example"
)


def get_db():
    db_name = os.environ.get("DB_NAME", "dev")
    return db_client[db_name]

