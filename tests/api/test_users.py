from conftest import client
import json


def test_get_users():
    response = client.get("/api/v1/users")
    assert response.status_code == 200


def test_create_user():
    response = client.post("/api/v1/users/", data=json.dumps({"name": "test1"}))
    assert response.status_code == 200
    assert "name" in response.json().get("user").keys()
    assert "test1" in response.json().get("user").get("name")
