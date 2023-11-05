def initialize(api):
    return Pipeline(api)

class Pipeline:
    def __init__(self, api) -> None:
        self._api = api
        self._name = "pipeline"

    def list(self):
        """
        Retrieves a list of pipelines from the API.

        Returns:
            A JSON object representing the existing list of pipelines.
        """
        response = self._api.get(self._name)
        return response.json()

    def add(self, params):
        pass

    def delete(self, params):
        pass

    def modify(self, params):
        pass
