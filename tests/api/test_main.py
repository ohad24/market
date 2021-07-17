from typing import Collection
from conftest import client
from db import get_db


class TestAPISetup:
    def test_settings(self):
        response = client.get("/info")
        data = response.json()
        assert response.status_code == 200
        assert data == {
            "db_name": "test",
            "db_host": "localhost",
            "db_password": "example",
            "db_username": "root",
        }

    def test_db_connection(self):
        db = get_db()
        assert "test" == db.name


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
