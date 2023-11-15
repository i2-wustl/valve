
from valve.core.api import create_client
import valve.core.resources.connectors as c
import valve.utils.logger as log
import os

__endpoint__ = "pipeline"

def list():
    """
    Retrieves a list of pipelines from the API.
    GET: /api/pipelines

    Returns:
        A JSON object representing the existing list of pipelines.
    """
    client = create_client()
    response = client.get(__endpoint__)
    return response


def add( pipeline):
    """
    Creates a new pipeline.
    POST: /api/pipelines

    Args:
        pipeline (Pipeline): The new pipeline data

    Returns:
        A JSON object representing the new pipeline.
    """
    client = create_client()
    response = client.post(__endpoint__, data=pipeline)
    return response

def delete(pipeline_id):
    """
    Adds a connector.
    DELETE: /api/connectors
    
    Returns:
        A JSON object representing the details associated with the new connector.
    """
    
    client = create_client()
    response = client.delete(__endpoint__, data={"pipelineId": pipeline_id})
    return response

def modify_artifacts(pipeline):
    """
    Modifies a pipeline to add multiple artifacts.
    PUT: /api/pipelines/artifacts

    Args:
        pipeline (Pipeline): The updated pipeline data

    Returns:
        A JSON object representing the updated pipeline.
    """
    client = create_client()
    response = client.post(__endpoint__ + "/artifacts", data=pipeline)
    return response

def add_tables_to_pipeline(id, connector_id, schema, tables):     
    items = c.get_ingestion_items(connector_id, schema, tables)

    data = {
    "pipelineID": id,
    "clientID": os.environ.get("API_CLIENT_ID", 0), # HACK: moving to API, remove this eventually
    "items": [
            
        ]
    }

    log.debug(items)
    for item in items["objects"]:
        #data["items"].append(item)
        data["items"].append(  {
            "artifactType": items["connectorType"],
            "ingestionType": item["ingestionType"],
            "sourceSchemaName": schema,
            "sourceTableName": item["tableName"],
            "sourceColumnNames": None,
            "mergeColumns": ",".join(item["mergeColumns"]),
            "targetSchemaName": None,
            "targetTableName": None,
            "sourceConnectionID": connector_id,
            "targetConnectionID": 0
        })

    result = modify_artifacts(data)  
    return result