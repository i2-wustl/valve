from valve.core.api import create_client
__endpoint__ = "connector"


def list():
    """
    Retrieves a list of connectors from the API.
    GET: /api/connectors

    Returns:
        A JSON object representing the existing list of connectors.
    """
    client = create_client()
    response = client.get(__endpoint__)
    return response

def list_catalogs(connector_id):
    """
    Retrieves a list of catalogs associated with a given connector.
    GET: /api/connectors/{connector_id}/catalogs

    Returns:
        A JSON object representing the existing list catalogs associated with a given connector.
    """

    endpoint = "/".join([__endpoint__, "catalogs", str(connector_id)])
    client = create_client()
    response = client.get(endpoint)
    return response

def list_catalog_tables(connector_id, catalog_name):
    """
    Retrieves a list of catalogs associated with a given connector.
    GET: /api/connectors/{connector_id}/tables?schemaCatalog={catalog_name}

    Returns:
        A JSON object representing the existing list catalogs associated with a given connector.
    """
    endpoint = (
        "/".join([__endpoint__, "tables", str(connector_id)])
        + f"?schemaCatalog={catalog_name}"
    )
    client = create_client()
    response = client.get(endpoint)
    return response

def get(connector_id):
    """
    Retrieves details on a single connector
    GET: /api/connectors/{connector_id}

    Returns:
        A JSON object representing the details associated with a given connector.
    """
    endpoint = "/".join([__endpoint__, str(connector_id)])
    client = create_client()
    response = client.get(endpoint)
    return response

def get_ingestion_items(connector_id, schema, tables):
    """
    Retrieves a list of table configurations to add to a pipelines.
    POST: /api/connector/ingestiontype

    Returns:
        A JSON object representing the existing list of pipelines.
    """
    client = create_client()
    response = client.post(
        __endpoint__ + "/ingestiontype",
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
    return response

def add(connector):
    """
    Adds a connector.
    POST: /api/connectors

    Returns:
        A JSON object representing the details associated with the new connector.
    """

    client = create_client()
    response = client.post(__endpoint__, data=connector)
    return response

def delete(connector_id):
    """
    Adds a connector.
    DELETE: /api/connectors

    Returns:
        A JSON object representing the details associated with the new connector.
    """

    client = create_client()
    response = client.delete(__endpoint__, data={"connectorID": connector_id})
    return response

def modify(connector):
    """
    Modify a connector.
    PUT: /api/connectors/

    Returns:
        A JSON object representing the details associated with the new connector.
    """

    client = create_client()
    response = client.put(__endpoint__, data=connector)
    return response
