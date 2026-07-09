def user_validation(users):

    if not isinstance(users,list):
        raise TypeError("users must be a list")

    user_list = []
    seen_ids = []

    for user in users:
        if user["email"].strip() == "":
            user_list.append(f"User with id {user['id']} has empty email")
        else:
            if "@" not in user["email"] or ".com" not in user["email"]:
                user_list.append(f"User with id {user['id']} has invalid email")

        if user["status"] not in ("active", "inactive", "blocked"):
            user_list.append(
                f"User with id {user['id']} has invalid status: {user['status']}"
            )

        if user["created_at"].strip() == "":
            user_list.append(f"User with id {user['id']} has empty created_at")

        if user["id"] in seen_ids:
            user_list.append(f"Duplicate user with id {user['id']}")
        else:
            seen_ids.append(user["id"])

    return user_list


def is_active_user(user):
    return user["status"] == "active"