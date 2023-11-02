import os
from valve.clients.base import BaseClient

class Oauth(BaseClient):
    _name = "auth"

    def login(self):
        client = self.get_client()
        response = client.post(os.getenv("X_API_BASE_URL") + "login", timeout=10, data="User/password")
        self.handle_response(response)
        
        json = response.json()    
        os.environ["X_API_TOKEN"] = json

        return json
    