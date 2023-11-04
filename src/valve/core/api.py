import os

import requests

import valve.utils.logger as log
from valve.core.resources import (
    users,
    connector,
    pipeline,
    access,
    config,
    tables
)

class API:
    def __init__(self, credentials=None, debug=False):
        if credentials is None:
            raise Exception("Please supply credentials to the API constructor")
        self.debug = debug
        self.credentials = credentials
        self._make_resource_properties()
        # import pdb
        # pdb.set_trace()

        self.root_url = credentials.url

    def debugger(self, msg, color=None):
        if self.debug:
            log.logit(msg, color=color)

    def _make_resource_properties(self):
        self.users = users.Users(self)
        self.connector = connector.Connector(self)
        self.pipeline = pipeline.Pipeline(self)
        self.access = access.Access(self)
        self.config = config.Config(self)
        self.tables = tables.Tables(self)

    def _get_auth_headers(self):
        return {
            "Accept": "application/json",
            "X-API-USER": self.credentials.user,
            "X-API-KEY": self.credentials.key,
        }

    def get(self, endpoint):
        headers = self._get_auth_headers()
        url = self._assemble_url(endpoint)
        self.debugger(f"root url: {url}", color='yellow')
        self.debugger(f"headers: {headers}", color='yellow')
        self.debugger("request type: GET", color='yellow')
        r = requests.get(url, headers=headers, verify=False)
        return r

    def _assemble_url(self, endpoint):
        # if not self.root_url.endswith("/api/"):
        #     self.root_url = os.path.join(self.root_url, "/api")
        return os.path.join(self.root_url, endpoint)
