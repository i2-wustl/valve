import os

from dotenv import load_dotenv
from valve.core.http_client_factory import HttpClientFactory

class BaseClient:
    def __init__(self):
        self._client_factory = HttpClientFactory()

    def get_client(self):
        client = self._client_factory.create()
        client.base_url += self._name  # Ensure self._name is defined

        # only add headers if they are defined
        api_user = os.getenv("X_API_USER", default=None)
        api_key = os.getenv("X_API_KEY", default=None)      
        api_token = OAuthClient.get_stored_creds()

        if api_user and api_key:
            client.headers.update({
                "Accept": "application/json",
                "x-api-user": api_user,
                "x-api-key": api_key
            })
        elif api_token:
             client.headers.update({
                "Accept": "application/json",
                "Authentication": "Bearer " + api_token
            })
        else:
            client.headers.update({
                "Accept": "application/json"
            })
      
        return client
    
    def handle_response(self, response):
        if response.status_code != 200:
            self._client_factory.handle_error(response)

class OAuthClient(BaseClient):

    _name = "auth"

    def login(self):
        #448dbb07-10ee-4c6a-91fd-a92f6bc8b987
        
        #open browser to oAuth url
   
        ## Register the client in Azure, grant https://management.azure.com/user_impersonation API permission to the App Registration
        # import azure-identity as ai
        # client = ai.AzureCliCredential()
        # client.authenticate()

        client = self.get_client()
        response = client.post(os.getenv("X_API_BASE_URL") + "login", timeout=10, data="User/password")
        self.handle_response(response)
        
        json = response.json()    
        os.environ["X_API_TOKEN"] = json

        # write json to file under users home directory
        if not os.path.exists(os.environ["HOME"] + "/.valve/"):
            os.makedirs(os.environ["HOME"] + "/.valve/")

        with open(os.environ["HOME"] + "/.valve/token.json", "w") as f:
            f.write(json)

        return json
    
    def get_stored_creds():
        api_token = os.getenv("X_API_TOKEN", default=None) 
        if api_token is not None:
            return api_token            
        else:
            if not os.path.exists(os.environ["HOME"] + "/.valve/"):
                return None

            if not os.path.exists(os.environ["HOME"] + "/.valve/token.json"):
                return None
                    
            with open(os.environ["HOME"] + "/.valve/token.json", "r") as f:
                return f.read()

class TokenClient(BaseClient):
    _name = "auth"

    def login(self):

        # Load environment variables from .env file
        load_dotenv()

        return ""
    