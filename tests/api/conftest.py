import sys
import os

sys.path.append("src/api/")
os.environ["DB_NAME"] = "test"

import main
import config
from fastapi.testclient import TestClient


# def get_settings_override():
#     return config.Settings(db_name="test")


client = TestClient(main.app)


# main.app.dependency_overrides[config.get_settings] = get_settings_override
