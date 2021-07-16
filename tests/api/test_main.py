from fastapi.testclient import TestClient
import sys

sys.path.append("src/api/")
from main import app
import json


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200


def test_create_user():
    headers = {"content-type": "application/json", "Accept": "application/json"}
    response = client.post(
        "/users", data=json.dumps({"name": "test1"}), headers=headers
    )
    print(response.json())
    assert response.status_code == 200
    assert "_id" in response.json().get("user").keys()
