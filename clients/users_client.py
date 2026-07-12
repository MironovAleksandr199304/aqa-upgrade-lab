import requests


class UsersClient:
    def __init__(self, base_url, timeout=5):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def get_user(self, user_id):
        return requests.get(
            f"{self.base_url}/users/{user_id}",
            timeout=self.timeout,
        )

    def create_user(self, json):
        response = requests.post(f"{self.base_url}/users", json=json, timeout=self.timeout)
        return response