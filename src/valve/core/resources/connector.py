def initialize(api):
    return Connector(api)

class Connector:
    def __init__(self, api) -> None:
        self._api = api
        self._name = "connector"

    def list(self):
        pass

    def add(self, params):
        pass

    def delete(self, params):
        pass

    def modify(self, params):
        pass
