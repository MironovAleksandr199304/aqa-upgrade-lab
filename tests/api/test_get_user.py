import pytest


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user_success(users_client, user_id):
    response = users_client.get_user(user_id)

    assert response.status_code == 200

    content_type = response.headers.get("Content-Type")

    assert content_type is not None, "Missing Content-Type header"
    assert "application/json" in content_type

    data = response.json()

    required_fields = ("id", "name", "email")

    for field in required_fields:
        assert field in data, f"Missing field: {field}"

    assert data["id"] == user_id

    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    assert isinstance(data["email"], str)


@pytest.mark.parametrize("user_id", [999999, 0, -1])
def test_get_user_not_found(users_client, user_id):
    response = users_client.get_user(user_id)

    assert response.status_code == 404
    assert response.json() == {}