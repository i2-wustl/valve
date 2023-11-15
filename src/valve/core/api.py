import requests
import valve.utils.logger as log
import valve.core.auth as auth
import os

def create_client():
    credentials = auth.login()
    client = API(credentials=credentials)
    return client

class API:
    def __init__(self, credentials=None):
        if credentials is None:
            raise Exception("Please supply credentials to the API constructor")

        self.credentials = credentials
        self.root_url = credentials.url

    def _assemble_url(self, endpoint):
        # if not self.root_url.endswith("/api/"):
        #     self.root_url = os.path.join(self.root_url, "/api")
        return os.path.join(self.root_url, endpoint)
    
    def _get_auth_headers(self):
        return {
            "Accept": "application/json",
            "X-API-USER": self.credentials.user,
            "X-API-KEY": self.credentials.key,
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
