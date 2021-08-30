from conftest import client, create_user, token_header
from db import get_db
from base_common import settings


create_user()


class TestAPISetup:
    def test_settings(self, token_header):
        response = client.get("/info", headers=token_header)
        data = response.json()
        assert response.status_code == 200
        assert data == settings.dict()

    def test_db_connection(self):
        db = get_db()
        assert "test" == db.name


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
