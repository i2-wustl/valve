def initialize(api):
    return Connector(api)


class Connector:
    def __init__(self, api) -> None:
        self._api = api
        self._name = "connector"

    def list(self):
        """
        Retrieves a list of connectors from the API.
        GET: /api/connectors

        Returns:
            A JSON object representing the existing list of connectors.
        """
        response = self._api.get(self._name)
        return response.json()

    def list_catalogs(self, connector_id):
        """
        Retrieves a list of catalogs associated with a given connector.
        GET: /api/connectors/{connector_id}/catalogs

        Returns:
            A JSON object representing the existing list catalogs associated with a given connector.
        """
        endpoint = "/".join([self._name, "catalogs", str(connector_id)])
        response = self._api.get(endpoint)
        return response.json()

    def list_catalog_tables(self, connector_id, catalog_name):
        """
        Retrieves a list of catalogs associated with a given connector.
        GET: /api/connectors/{connector_id}/tables?schemaCatalog={catalog_name}

        Returns:
            A JSON object representing the existing list catalogs associated with a given connector.
        """
        endpoint = (
            "/".join([self._name, "tables", str(connector_id)])
            + f"?schemaCatalog={catalog_name}"
        )
        response = self._api.get(endpoint)
        return response.json()

    def get(self, connector_id):
        """
        Retrieves details on a single connector
        GET: /api/connectors/{connector_id}

        Returns:
            A JSON object representing the details associated with a given connector.
        """
        endpoint = "/".join([self._name, str(connector_id)])
        response = self._api.get(endpoint)
        return response.json()

    def get_ingestion_items(self, connector_id, schema, tables):
        """
        Retrieves a list of table configurations to add to a pipelines.
        POST: /api/connector/ingestiontype

        Returns:
            A JSON object representing the existing list of pipelines.
        """
        response = self._api.post(
            self._name + "/ingestiontype",
            data={
                "connectorID": connector_id,
                "chosenDatabaseSchema": schema,
                "objects": tables.split(","),
                "connectorType": "test",
                "connectorDatabase": "test",
                "connectorName": "test",
                "connectorTechnology": "test",
            },
        )
        return response.json()

    def add(self, connector):
        """
        Adds a connector.
        POST: /api/connectors

        Returns:
            A JSON object representing the details associated with the new connector.
        """

        response = self._api.post(self._name, data=connector)
        return response.json()

    def delete(self, connector_id):
        """
        Adds a connector.
        DELETE: /api/connectors

        Returns:
            A JSON object representing the details associated with the new connector.
        """

        response = self._api.delete(self._name, data={"connectorID": connector_id})
        return response.json()

    def modify(self, connector):
        """
        Adds a connector.
        PUT: /api/connectors/

        Returns:
            A JSON object representing the details associated with the new connector.
        """

        response = self._api.put(self._name, data=connector)
        return response.json()
