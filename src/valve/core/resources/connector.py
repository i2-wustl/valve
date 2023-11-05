def initialize(api):
    return Connector(api)

class Connector:
    def __init__(self, api) -> None:
        self._api = api
        self._name = "connector"

    def list(self):
        """
        Retrieves a list of connectors from the API.

        Returns:
            A JSON object representing the existing list of connectors.
        """
        response = self._api.get(self._name)
        return response.json()

    def list_catalog(self, connector_id):
        """
        Retrieves a list of catalogs associated with a given connector.

        Returns:
            A JSON object representing the existing list catalogs associated with a given connector.
        """
        endpoint = '/'.join([self._name, 'catalogs', str(connector_id)])
        response = self._api.get(endpoint)
        return response.json()

    def add(self, params):
        pass

    def delete(self, params):
        pass

    def modify(self, params):
        pass
