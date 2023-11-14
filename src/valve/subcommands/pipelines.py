import click

import valve.core.api as api
import valve.core.auth
import valve.utils.printer as pp

import requests
import inquirer
import os

@click.group("pipelines")
def pipelines():
    pass

@pipelines.command("list", short_help="show pipeline list")
@click.option('--debug', '-d', is_flag=True, show_default=True, default=False,
              help="Print extra debugging output")
@click.option('--format', '-f', default="json", required=False, type=click.Choice(pp.valid_formats),
              help="output format")
def list_pipelines(debug, format):
    """
    Show pipelines list
    """
    credentials = valve.core.auth.login(debug=debug)
    client = api.API(debug=debug, credentials=credentials)
    pipelines = client.pipelines.list()
    printer = pp.Printer(pipelines)
    printer.render(format=format)




@pipelines.command("add-table", short_help="Add a table to a pipeline")
@click.option('--id', type=click.INT, required=True)
@click.option('--source-id', type=click.INT, required=True)
@click.option('--ingestion-type', type=click.Choice(['snapshot', 'delta']), required=True)
@click.option('--schema', type=click.STRING, required=True)
@click.option('--table', type=click.STRING, required=True)
@click.option('--columns', type=click.STRING, required=False, default=None)
@click.option('--merge-columns', type=click.STRING, required=False, default=None)
@click.option('--watermark-column', type=click.STRING, required=False, default=None)
@click.option('--retention', type=click.INT, required=False, default=None)
@click.option('--debug', '-d', is_flag=True, show_default=True, default=False,
              help="Print extra debugging output")
@click.option('--format', '-f', default="json", required=False, type=click.Choice(pp.valid_formats),
              help="output format")
def update_pipeline(debug, format, id, source_id, ingestion_type, schema, table, columns, merge_columns, watermark_column, retention):
    """
    Updates a pipeline and adds a table to it
    """

    if ingestion_type == 'snapshot':
        if retention is None:
            retention = 3
    elif ingestion_type == 'delta':
        if watermark_column is None:
            raise Exception("Watermark column is required for delta ingestion type")
        if merge_columns is None:
            raise Exception("Merge columns are required for delta ingestion type")

    credentials = valve.core.auth.login(debug=debug)
    client = api.API(debug=debug, credentials=credentials)

    data = {
    "pipelineID": id,
    "clientID": os.environ.get("API_CLIENT_ID", 0), # Question: How to determine this?
    "items": [
            {
                "artifactType": "database",
                "ingestionType": ingestion_type,
                "sourceConnectionID": source_id,
                "sourceSchemaName": schema,
                "sourceTableName": table,
                "sourceColumnNames": columns,
                "mergeColumns": merge_columns,
                "watermarkColumnName": watermark_column,
                "snapshotRetentionNum": retention,
                "targetConnectionID": 0,
                "targetSchemaName": None,
                "targetTableName": None
            }
        ]
    }

    try:
        result = client.pipelines.modify(data)               
        printer = pp.Printer(result)
        printer.render(format=format)
    except requests.RequestException as e:
        print(f"Error submitting data: {e}")


@pipelines.command("add-clarity-tables", short_help="Adds multiple tables to the Clarity pipeline")
@click.argument('tables', type=click.STRING)
@click.option('--debug', '-d', is_flag=True, show_default=True, default=False,
              help="Print extra debugging output")
@click.option('--format', '-f', default="json", required=False, type=click.Choice(pp.valid_formats),
              help="output format")
def update_clarity_pipeline(debug, format, tables):
    # credentials = valve.core.auth.login(debug=debug)
    # client = api.API(debug=debug, credentials=credentials)

    # data = {
    #     "pipelineID": 123, #TODO: update for correct value
    # }
    # ingestion_type = 'snapshot'
    # source_connector_id = 10 #Note: Hardcoded for clarity #TODO: update for correct value
    # source_column_names = None
    # source_schema_name = 'ORGFILTER'
    # target_connector_id = 0 #Question: How to determine this?
    # target_schema_name = None
    # target_table_name = None
    # merge_columns = None
    # wartermark_column_name = None
    # snapshot_retention_num = 3

    # Split table string buy comma
    tables = tables.split(',')
    #_tables = []
    # for each table in the list add a dict object to the data.items array
    for table in tables:
        update_pipeline(debug=debug, format=format, id=123, source_id=10, 
                        ingestion_type='snapshot', schema='ORGFILTER', 
                        table=table, columns=None, merge_columns=None, watermark_column=None, retention=3)
        # _tables.append({
        #   "artifactType": "database",
        #   "ingestionType": ingestion_type,
        #   "sourceSchemaName": source_schema_name,
        #   "sourceTableName": table,
        #   "sourceColumnNames": source_column_names,
        #   "mergeColumns": merge_columns,
        #   "targetSchemaName": target_schema_name,
        #   "targetTableName": target_table_name,
        #   "sourceConnectionID": source_connector_id,
        #   "targetConnectionID": target_connector_id,
        #   "watermarkColumnName": wartermark_column_name,
        #   "snapshotRetentionNum": snapshot_retention_num
        # })
    
    # data["items"] = _tables
    # result = client.pipelines.modify(data)
    # printer = pp.Printer(result, debug=debug)
    # printer.render(format=format)


@pipelines.group("tables", short_help="manage pipeline tables")
def pipelines_tables():
    pass


def add_table_wizard(client, debug, format):
    client = client
    user_data = {}


    def select_pipeline():
        result = client.pipelines.list()
        
        #map results to list of dicts containing ids and names
        _pipelines = [{"id": r["pipelineID"], "name": r["pipelineName"]} for r in result]

        questions = [
            inquirer.List('choice', 
                          message="Select your pipeline",
                          choices=_pipelines,
                          carousel=True),
        ]
        return inquirer.prompt(questions)

    def select_source_connector():
        result = client.connectors.list()
        
        #map results to list of dicts containing ids and names
        _connectors = [{"id": r["connectorID"], "name": r["connectorName"]} for r in result]

        questions = [
            inquirer.List('choice', 
                          message="Select the source connector",
                          choices=_connectors,
                          carousel=True),
        ]
        return inquirer.prompt(questions)

    def specify_tables():
        questions = [
            inquirer.Text('info', message="Enter the tables you want to add, separated by commas in the format <schema>.<table>"),
        ]
        return inquirer.prompt(questions)

    # Step 1
    selected_pipeline = select_pipeline()
    user_data["pipelineID"] = selected_pipeline["choice"]["id"]

    # Step 2 (conditional)
    source_connector = select_source_connector()
    source_connector_id = source_connector["choice"]["id"]
    

    # Final Step (can add more steps similarly)
    tables = specify_tables()

    # Split tables by comma and convert to list
    tables = tables["info"].split(",")

    ingestion_type = 'snapshot'   
    source_column_names = None
    target_connector_id = 0 #Question: How to determine this?
    target_schema_name = None
    target_table_name = None
    merge_columns = None
    wartermark_column_name = None
    snapshot_retention_num = 3

    user_data["items"] = []
    #For each table in list add an object to user_data["items"]
    for table in tables:
        # Split the table by period, use the first part as source schema name and second part as table name
        source_schema_name, source_table_name = table.split(".")
        user_data["items"].append(
            {
          "artifactType": "database",
          "ingestionType": ingestion_type,
          "sourceSchemaName": source_schema_name,
          "sourceTableName": source_table_name,
          "sourceColumnNames": source_column_names,
          "mergeColumns": merge_columns,
          "targetSchemaName": target_schema_name,
          "targetTableName": target_table_name,
          "sourceConnectionID": source_connector_id,
          "targetConnectionID": target_connector_id,
          "watermarkColumnName": wartermark_column_name,
          "snapshotRetentionNum": snapshot_retention_num
        })

    return user_data

@pipelines_tables.command("add", short_help="add tables to a pipeline")
@click.option('--debug', '-d', is_flag=True, show_default=True, default=False,
              help="Print extra debugging output")
@click.option('--format', '-f', default="json", required=False, type=click.Choice(pp.valid_formats),
              help="output format")
def add_tables_to_pipeline_wizard(debug, format):
    credentials = valve.core.auth.login(debug=debug)
    client = api.API(debug=debug, credentials=credentials)    
    data = add_table_wizard(client, debug, format)
    
    try:
        client.pipelines.modify(data)               
        print("Data submitted successfully!")
    except requests.RequestException as e:
        print(f"Error submitting data: {e}")


