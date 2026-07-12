def assert_json_content_type(response):
    content_type = response.headers.get("Content-Type")
    assert "application/json" in content_type

def assert_required_fields(data, required_fields):
    for field in required_fields:
        assert field in data, f"Missing field: {field}"

def assert_field_types(data, expected_types):
    for field, expected_type in expected_types.items():
        assert isinstance(data[field], expected_type), (
            f"Field '{field}' has invalid type. "
            f"Expected: {expected_type.__name__}, "
            f"actual: {type(data[field]).__name__}"
        )