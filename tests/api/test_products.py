from conftest import client
import json
from models.product import Product


def test_get_products(product_data):
    response = client.get("/api/v1/products")
    assert response.status_code == 200
    assert Product(**(response.json().get("products")[-1])) == product_data


def test_create_product(store_data):
    response = client.post(
        "/api/v1/products/",
        data=json.dumps(
            {
                "name": "product1",
                "description": "product desc 1",
                "store_id": store_data.store_id,
            }
        ),
    )
    assert response.status_code == 200
    assert "name" in response.json().get("product").keys()
    assert "product1" in response.json().get("product").get("name")

    response = client.post(
        "/api/v1/products/",
        data=json.dumps(
            {
                "name": "product1",
                "description": "product desc 1",
                "store_id": store_data.store_id + "a",
            }
        ),
    )
    assert response.status_code == 422
