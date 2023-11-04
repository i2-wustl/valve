import os
import tomli

import valve.utils.logger as log

def login(user=None, key=None, url=None, debug=False):
    credentials = Auth(user=user, key=key, url=url, debug=debug)
    return credentials

class Auth():
    def __init__(self, user, key, url, debug=False):

        self.debug = debug
        self.config_path = os.path.join(os.environ['HOME'], '.config/valve', 'config.toml')

        if user and key and url:
            self.debugger("Authenticating by user supplied parameters", color='yellow')
            self.user = user
            self.key = key
            self.url = url
        elif self.ensure_environment_variables():
            self.debugger("Authenticating by environment variables", color='yellow')
            self.user = os.environ['X_API_USER']
            self.key = os.environ['X_API_KEY']
            self.url = os.environ['X_API_URL']
        elif self.ensure_configuration_file():
            self.debugger(f"Authenticating by configuration file: {self.config_path}", color='yellow')
            (user, key, url) = self.parse_configuration_file()
            self.user = user
            self.key = key
            self.url = url

    def debugger(self, msg, color=None):
        if self.debug:
            log.logit(msg, color=color)

    def ensure_environment_variables(self):
        env_vars = ['X_API_USER', 'X_API_KEY', 'X_API_URL']
        for v in env_vars:
            if v not in os.environ:
                return False
#                msg = f"[err] environment variable '{v}' is not specified, please set it!"
#                raise Exception(msg)
        return True

    def ensure_configuration_file(self):
        if not os.path.exists(self.config_path):
            msg = f"[err] Could not find valve config file: '{self.config_path}'"
            raise FileNotFoundError(msg)
        return True

    def parse_configuration_file(self):
        config = None
        with open(self.config_path, mode='rb') as f:
            config = tomli.load(f)
        user = config['credentials']['user']
        key = config['credentials']['key']
        url = config['credentials']['url']
        return (user, key, url)

    def __str__(self):
        cls = self.__class__
        return f"<{cls.__module__} user:{self.user} key:{self.key} url:{self.url}> object at {id(self)}"
