import os
from valve.core.http_client_factory import HttpClientFactory

class BaseClient:
    def __init__(self):
        self._client_factory = HttpClientFactory()

    def get_client(self):
        client = self._client_factory.create()
        client.base_url += self._name  # Ensure self._name is defined
        client.headers.update({
            "Accept": "application/json",
            "x-api-user": os.getenv("X_API_USER"),
            "x-api-key": os.getenv("X_API_KEY")
        })
        return client
    
    def handle_response(self, response):
        if response.status_code != 200:
            self._client_factory.handle_error(response)