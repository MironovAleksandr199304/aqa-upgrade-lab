import pytest

from utilites.users_validation import user_validation, is_active_user


def test_validate_users_success(valid_user):
    result = user_validation(valid_user)

    assert result == []


def test_empty_email_validation():
    empty_email_user = [
        {
            "id": 1,
            "email": "",
            "status": "active",
            "created_at": "2026-07-03",
        }
    ]

    result = user_validation(empty_email_user)

    assert result == [
        f"User with id {empty_email_user[0]['id']} has empty email"
    ]


def test_invalid_email_validation():
    invalid_email_user = [
        {
            "id": 1,
            "email": "mironovav1993gmail.com",
            "status": "active",
            "created_at": "2026-07-03",
        }
    ]

    result = user_validation(invalid_email_user)

    assert result == [
        f"User with id {invalid_email_user[0]['id']} has invalid email"
    ]


def test_invalid_status_validation():
    invalid_status_user = [
        {
            "id": 1,
            "email": "mironovav1993@gmail.com",
            "status": "invalid",
            "created_at": "2026-07-03",
        }
    ]

    result = user_validation(invalid_status_user)

    assert result == [
        f"User with id {invalid_status_user[0]['id']} has invalid status: {invalid_status_user[0]['status']}"
    ]


def test_empty_created_at_validation():
    empty_created_at_user = [
        {
            "id": 1,
            "email": "mironovav1993@gmail.com",
            "status": "active",
            "created_at": "",
        }
    ]

    result = user_validation(empty_created_at_user)

    assert result == [
        f"User with id {empty_created_at_user[0]['id']} has empty created_at"
    ]


def test_duplicate_id_validation():
    duplicate_id_user = [
        {
            "id": 1,
            "email": "mironovav1993@gmail.com",
            "status": "active",
            "created_at": "2026-07-03",
        },
        {
            "id": 1,
            "email": "mironovav@gmail.com",
            "status": "active",
            "created_at": "2026-07-03",
        },
    ]

    result = user_validation(duplicate_id_user)

    assert result == [
        f"Duplicate user with id {duplicate_id_user[1]['id']}"
    ]


@pytest.mark.parametrize(
    "user, expected_result",
    [
        (
            {
                "id": 1,
                "email": "a@test.com",
                "status": "active",
                "created_at": "2026-07-03",
            },
            True,
        ),
        (
            {
                "id": 2,
                "email": "b@test.com",
                "status": "inactive",
                "created_at": "2026-07-03",
            },
            False,
        ),
        (
            {
                "id": 3,
                "email": "c@test.com",
                "status": "blocked",
                "created_at": "2026-07-03",
            },
            False,
        ),
    ],
)
def test_active_status_validation(user, expected_result):
    result = is_active_user(user)

    assert result is expected_result