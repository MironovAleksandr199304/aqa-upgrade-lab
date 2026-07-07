import pytest


@pytest.fixture
def valid_user():
    return [
        {
            "id": 1,
            "email": "mironovav1993@gmail.com",
            "status": "active",
            "created_at": "2026-07-03",
        }
    ]