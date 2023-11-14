import os
import sys
import importlib
import json

import requests
from valve.core.resources.access import Access
from valve.core.resources.connector import Connector
from valve.core.resources.teams import Teams
from valve.core.resources.pipeline import Pipeline
from valve.core.resources.tables import Tables
from valve.core.resources.users import Users
from valve.core.resources.config import Config

import valve.utils.logger as log

databasin_resources = [
    'users',
    'connector',
    'pipeline',
    'access',
    'config',
    'tables',
]

#TODO: Implement global error handling for API calls

class API:
    def __init__(self, credentials=None, debug=False, databasin_resources=databasin_resources):
        if credentials is None:
            raise Exception("Please supply credentials to the API constructor")
        self.debug = debug
        self.credentials = credentials
        #self.resource_properties = databasin_resources
        #self._make_resource_properties()
        # import pdb
        # pdb.set_trace()
        self.pipelines = Pipeline(self)
        self.users = Users(self)
        self.teams = Teams(self)
        self.connectors = Connector(self)
        # Question: do we need these after the access / storage refactor?
        # self.access = Access(self)
        # self.config = Config(self)
        self.tables = Tables(self)
        
        self.root_url = credentials.url

    def debugger(self, msg, color=None):
        if self.debug:
            log.logit(msg, color=color)

    def _make_resource_properties(self):
        for resource in self.resource_properties:
            module_name = '.'.join(['valve.core.resources', resource])
            self.debugger(f"Adding resource property: '{resource}' -- '{module_name}' to api", color='yellow')
            # dynamically load the module at runtime
            importlib.import_module(module_name)
            # dynamically add the resource attribute at runtime to the api object
            module = sys.modules[module_name]
            setattr(self, resource, module.initialize(self))

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
    def put(self, endpoint, data):
        headers = self._get_auth_headers()
        url = self._assemble_url(endpoint)
        self.debugger(f"root url: {url}", color='yellow')
        self.debugger(f"headers: {headers}", color='yellow')
        self.debugger("request type: PUT", color='yellow')
        r = requests.put(url, headers=headers, json=json.dumps(data), verify=False)
        return r
    def post(self, endpoint, data):
        headers = self._get_auth_headers()
        url = self._assemble_url(endpoint)
        self.debugger(f"root url: {url}", color='yellow')
        self.debugger(f"headers: {headers}", color='yellow')
        self.debugger("request type: POST", color='yellow')
        r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
        return r
    def delete(self, endpoint, data):
        headers = self._get_auth_headers()
        url = self._assemble_url(endpoint)
        self.debugger(f"root url: {url}", color='yellow')
        self.debugger(f"headers: {headers}", color='yellow')
        self.debugger("request type: DELETE", color='yellow')
        
        r = requests.delete(url, headers=headers, data=json.dumps(data), verify=False)
        return r    
    def _assemble_url(self, endpoint):
        # if not self.root_url.endswith("/api/"):
        #     self.root_url = os.path.join(self.root_url, "/api")
        return os.path.join(self.root_url, endpoint)

    def __str__(self):
        cls = self.__class__
        return "\n".join([
            f"<{cls.__module__}",
            f"\tdebug:{self.debug}",
            f"\tcredentials:{self.credentials}",
            f"\troot_url:{self.root_url}",
            f"\tresource_properties:{self.resource_properties}>",
            f"object at {id(self)}"
        ])
