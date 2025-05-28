import json
import os
import pytest


@pytest.fixture
def user_data():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "fixtures", "user_data.json")
    with open(file_path, encoding="utf-8") as f:
        return json.load(f)


