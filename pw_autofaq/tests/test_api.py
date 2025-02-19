import pytest
from pages.api_client import APIClient
from data.payloads import payload


class TestChatApi:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.api_client = APIClient()

    def test_open_chat(self):
        res = self.api_client.open_chat()
        assert res.status_code == 204, "Chat wasn`t open"

    def test_user_details(self):
        res = self.api_client.pass_user_details(payload=payload)
        assert res.status_code == 200
        assert res.json()["email"] == payload["email"], "Email does not match"
        assert res.json()["fullName"] == payload['fullName'], "Full name does not match"
        print(res.json())


