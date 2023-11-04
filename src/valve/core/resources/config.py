def initialize(api):
    return Config(api)

class Config:
    def __init__(self, api) -> None:
        self._api = api
        self._name = "config"

    def list(self):
        pass

    def add(self, params):
        pass

    def delete(self, params):
        pass

    def modify(self, params):
        pass
