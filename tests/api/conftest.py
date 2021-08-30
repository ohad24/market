import sys
import os

from requests.models import Response

sys.path.append("src/api/")
os.environ["DB_NAME"] = "test"

import main

# import config
from fastapi.testclient import TestClient
import pytest
from models.store import Store
from models.product import Product
from db import get_db
import json


# def get_settings_override():
#     return config.Settings(db_name="test")


client = TestClient(main.app)


# main.app.dependency_overrides[config.get_settings] = get_settings_override


@pytest.fixture(scope="module")
def store_data():
    db = get_db()
    ret = db.stores.insert_one(
        Store(**{"name": "store1", "description": "store desc 1"}).dict(by_alias=True)
    )
    store_date = db.stores.find_one({"_id": ret.inserted_id})
    store = Store(**store_date)
    return store


@pytest.fixture(scope="module")
def product_data(store_data):
    db = get_db()
    ret = db.products.insert_one(
        Product(
            **{
                "name": "product1",
                "description": "product desc 1",
                "store_id": store_data.store_id,
            }
        ).dict(by_alias=True)
    )
    product_date = db.products.find_one({"_id": ret.inserted_id})
    product = Product(**product_date)
    return product


# @pytest.fixture()
def create_user(): # TODO: use the API and fixture
    response = client.post(
        "/api/v1/users/", data=json.dumps({"name": "test11", "password": "1234"})
    )


@pytest.fixture
def token_header():
    response = client.post(
        "/token",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data="username=test11&password=1234",
    )
    auth_data = response.json()
    return {
        "Authorization": f"{auth_data.get('token_type')} {auth_data.get('access_token')}"
    } # TODO: use token model
