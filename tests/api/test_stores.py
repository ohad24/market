from conftest import client
import json


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


def test_get_store(store_data):
    response = client.get(f"/api/v1/stores/{store_data.store_id}")
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
