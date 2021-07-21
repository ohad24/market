from conftest import client
import json
import pytest


@pytest.fixture(scope="module")
def data():
    pytest.store_id = None


def test_get_stores():
    response = client.get("/api/v1/stores")
    assert response.status_code == 200


def test_create_store(data):
    response = client.post(
        "/api/v1/stores/",
        data=json.dumps({"name": "store1", "description": "store desc 1"})
    )
    assert response.status_code == 200
    assert "name" in response.json().get("store").keys()
    assert "store1" in response.json().get("store").get("name")
    pytest.store_id = response.json().get("store").get("store_id")


def test_get_store(data):
    if not pytest.store_id:
        test_create_store(data)
    response = client.get(f"/api/v1/stores/{pytest.store_id}")
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200

    response = client.get(f"/api/v1/stores/{pytest.store_id}" + "a")
    assert response.status_code == 404
