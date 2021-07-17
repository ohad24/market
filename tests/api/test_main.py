from fastapi.testclient import TestClient
import sys

sys.path.append("src/api/")
import main
import json

client = TestClient(main.app)


# def get_settings_override():
#     return config.Settings(db_name="test")


# main.app.dependency_overrides[config.get_settings] = get_settings_override


def test_settings():
    response = client.get("/info")
    data = response.json()
    assert data == {}


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


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
