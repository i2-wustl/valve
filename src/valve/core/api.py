import os
import valve.utils.logger as log
import requests


def hello(debug):
    if debug:
        log.logit("Hello There! (with debug flag)", color="yellow")
    else:
        log.logit("Hello There!")


class API:    
    def __init__(self):
        pass
    
    def init(self, credentials=None):
        self._makeProperties()
        if credentials is None:
            raise Exception("Please supply credentials to the API constructor")
        self.credentials = credentials
        # import pdb
        # pdb.set_trace()

        self.root_url = credentials.url
        return self
    
    def _makeProperties(self):
        self.users = Users(self)
        #self.connector = Connectors(self)
            
    def _get_auth_headers(self):
        return {
            "Accept": "application/json",
            "X-API-USER": self.credentials.user,
            "X-API-KEY": self.credentials.key,
        }

    def get(self, endpoint):
        headers = self._get_auth_headers()
        r = requests.get(self._assemble_url(endpoint), headers=headers, verify=False)
        return r

    def _assemble_url(self, endpoint):
        # if not self.root_url.endswith("/api/"):
        #     self.root_url = os.path.join(self.root_url, "/api")
        return os.path.join(self.root_url, endpoint)

class Users:
    def __init__(self, api) -> None:
        self._api = api
        self._name = "users"

    def list(self):
        """
        Retrieves a list of items from the API.

        Returns:
            A JSON object representing the list of items.
        """
        response = self._api.get(self._name)
        return response.json()
    
    def add(self, params):
        response = self._api.post(self._name, params)
        return response.json()

    # def delete(self, params):
    #     client = self.get_client()
    #     response = client.delete("", json=params, timeout=10)
    #     client.handle_response(response)
    #     return response.json()

    # def modify(self, params):
    #     client = self.get_client()
    #     response = client.put("", json=params, timeout=10)
    #     client.handle_response(response)
    #     return response.json()