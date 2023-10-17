import os
from valve.core.base_client import BaseClient

class UsersClient(BaseClient):
    _name = "users"

    def list(self):
        client = self.get_client()
        response = client.get(os.getenv("X_API_BASE_URL") + "users", timeout=10)
        self.handle_response(response)
        return response.json()

    def add(self, params):
        client = self.get_client()
        response = client.post("", json=params, timeout=10)
        client.handle_response(response)
        return response.json()

    def delete(self, params):
        client = self.get_client()
        response = client.delete("", json=params, timeout=10)
        client.handle_response(response)
        return response.json()

    def modify(self, params):
        client = self.get_client()
        response = client.put("", json=params, timeout=10)
        client.handle_response(response)
        return response.json()

    def auth(self, params):
        client = self.get_client()
        response = client.post("/auth", json=params, timeout=10)
        client.handle_response(response)
        return response.json()
