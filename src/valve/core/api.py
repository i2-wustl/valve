import valve.utils.logger as log
import requests

def hello(debug):
    if debug:
        log.logit("Hello There! (with debug flag)", color="yellow")
    else:
        log.logit("Hello There!")

class API():
    def __init__(self, credentials=None):
        if credentials is None:
            raise Excception("Please supply credentials to the API constructor")
        self.credentials = credentials
        self.root_url = credentials.url

    def _get_auth_headers(self):
        return {
            'X_API_USER' : self.credentials.user,
            'X_API_KEY' : self.credentials.key,
        }

    def _get(self, endpoint):
        headers = self._get_auth_headers()
        r = requests.get(self.root_url, headers=headers)


    def get_users(self):
        route = '/api/users'
        response = self._get(route)
        return response.json()
