from conftest import client
import json
import pytest
from db import get_db
from models.store import Store
from models.product import Product


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


def test_get_stores():
    response = client.get("/api/v1/stores")
    assert response.status_code == 200


def test_create_store():
    response = client.post(
        "/api/v1/stores/",
        data=json.dumps({"name": "store1", "description": "store desc 1"}),
    )
    assert response.status_code == 200
    assert "name" in response.json().get("store").keys()
    assert "store1" in response.json().get("store").get("name")
    # pytest.store_id = response.json().get("store").get("store_id")


def test_get_store(store_data):
    response = client.get(f"/api/v1/stores/{store_data.store_id}")
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200

    response = client.get(f"/api/v1/stores/{store_data.store_id}" + "a")
    assert response.status_code == 404


def test_get_products_in_store(product_data):
    response = client.get(f"/api/v1/stores/{product_data.store_id}/products")
    assert response.status_code == 200
    assert "products" in response.json().get("store").keys()
    assert "product1" in response.json().get("store").get("products")[0].get("name")

    response = client.get(f"/api/v1/stores/{product_data.store_id}a/products")
    assert response.status_code == 404
