import pytest
from clients.users_client import UsersClient

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

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def users_client(base_url):
    return UsersClient(base_url)