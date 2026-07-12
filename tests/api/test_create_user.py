from helpers.api_assertions import assert_field_types, assert_required_fields, assert_json_content_type


def test_create_user_success(users_client):

    payload = {
        "name": "SashaAQA",
        "email": "mironovsasha199304@gmail.com"
    }

    expected_types = {
        "id": int,
        "name": str,
        "email": str,
    }

    response = users_client.create_user(payload)
    assert response.status_code == 201

    assert_json_content_type(response)

    data = response.json()

    required_fields = ("id", "name", "email")
    assert_required_fields(data, required_fields)

    assert_field_types(data, expected_types)

    for field in payload:
        assert data[field] == payload[field]


