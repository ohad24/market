from conftest import client
import json


def test_get_users():
    response = client.get("/api/v1/users")
    assert response.status_code == 200


def test_create_user():
    headers = {"content-type": "application/json", "Accept": "application/json"}
    response = client.post(
        "/api/v1/users/",
        data=json.dumps({"name": "test1"}),
        headers=headers,
    )
    assert response.status_code == 200
    assert "_id" in response.json().get("user").keys()
