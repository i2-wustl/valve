import requests
import valve.utils.logger as log
import os
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential


def create_client():
    #credentials = auth.login()
    credentials = DefaultAzureCredential(logging_enable=True,
        exclude_cli_credential=True,
        interactive_browser_tenant_id="4ccca3b5-71cd-4e6d-974b-4d9beb96c6d6",
        interactive_browser_client_id="0f60d342-8fcc-4009-8a49-ab7760d896b2",
        exclude_interactive_browser_credential=False)
    
    credentials = InteractiveBrowserCredential(logging_enable=True,
        exclude_cli_credential=True,
        tenant_id="4ccca3b5-71cd-4e6d-974b-4d9beb96c6d6",
        client_id="0f60d342-8fcc-4009-8a49-ab7760d896b2",
        redirect_uri="https://databasin.wustl.edu/login")
    
    client = API(credentials=credentials)
    return client

class API:
    def __init__(self, credentials=None):
        if credentials is None:
            raise Exception("Please supply credentials to the API constructor")

        self.credentials = credentials
        self.root_url = "https://api.databasin.wustl.edu/api"
        # scope="00000003-0000-0000-c000-000000000000/.default"
        #scope="api://0f60d342-8fcc-4009-8a49-ab7760d896b2/.default"
        #scope="2ff814a6-3304-4ab8-85cb-cd0e6f879c1d/.default"
        # scope="api://0f60d342-8fcc-4009-8a49-ab7760d896b2/Databasin.API"
        # scope="api://0f60d342-8fcc-4009-8a49-ab7760d896b2/Databasin.Hierarchies"
        scope="api://da78a353-fd13-4707-b327-4c91f0f2a7d1/Databasin.Hierarchies"
        self.access_token = self.credentials.get_token(scope)
        print(self.access_token)

    def _assemble_url(self, endpoint):
        # if not self.root_url.endswith("/api/"):
        #     self.root_url = os.path.join(self.root_url, "/api")
        return os.path.join(self.root_url, endpoint)
    
    def _get_auth_headers(self):

        
        return {
            "Accept": "application/json",
            "Authorization": f"Bearer: {self.access_token.token}"
        }

    def _log_request_details(self, request_type, headers, url):
        log.debug(f"root url: {url}", color="yellow")
        log.debug(f"headers: {headers}", color="yellow")
        log.debug(f"request type: {request_type}", color="yellow")

    def get(self, endpoint=None):
        result = None
        try:
            headers = self._get_auth_headers()
            endpoint_url = self._assemble_url(endpoint)
            self._log_request_details("GET", headers, endpoint_url)
            result = requests.get(endpoint_url, headers=headers, verify=False)
            if result.status_code == 200:
                result = result.json()
            else:
                result = {"error": result.status_code, "msg": result.text}
                log.logit(result, color="red")
        except Exception as ex:
            log.logit(ex, color="red")
        finally:
            return result

    def put(self, endpoint, data):
        try:
            headers = self._get_auth_headers()
            endpoint_url = self._assemble_url(endpoint)
            self._log_request_details("PUT", headers, endpoint_url)
            result = requests.put(
                endpoint_url, headers=headers, json=data, verify=False
            )
            if result.status_code == 200:
                result = result.json()
            else:
                result = {"error": result.status_code, "msg": result.text}
                log.logit(result, color="red")
        except Exception as ex:
            log.logit(ex, color="red")
        finally:
            return result

    def post(self, endpoint, data):
        try:
            headers = self._get_auth_headers()
            endpoint_url = self._assemble_url(endpoint)
            self._log_request_details("POST", headers, endpoint_url)
            result = requests.post(
                endpoint_url, headers=headers, json=data, verify=False
            )
            if result.status_code == 200:
                result = result.json()
            else:
                result = {"error": result.status_code, "msg": result.text}
                log.logit(result, color="red")
        except Exception as ex:
            log.logit(ex, color="red")
        finally:
            return result

    def delete(self, endpoint, data):
        try:
            headers = self._get_auth_headers()
            endpoint_url = self._assemble_url(endpoint)
            self._log_request_details("DELETE", headers, endpoint_url)
            result = requests.delete(
                endpoint_url, headers=headers, json=data, verify=False
            )
            if result.status_code == 200:
                result = result.json()
            else:
                result = {"error": result.status_code, "msg": result.text}
                log.logit(result, color="red")
        except Exception as ex:
            log.logit(ex, color="red")
        finally:
            return result

    def __str__(self):
        cls = self.__class__
        return "\n".join(
            [
                f"<{cls.__module__}",
                f"\tdebug:{self.debug}",
                f"\tcredentials:{self.credentials}",
                f"\troot_url:{self.root_url}",
                f"\tresource_properties:{self.resource_properties}>",
                f"object at {id(self)}",
            ]
        )
