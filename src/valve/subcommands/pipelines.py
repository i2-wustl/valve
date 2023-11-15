import click
import valve.utils.printer as pp
import valve.utils.logger as log
import valve.core.resources.pipelines as p
import valve.core.resources.connectors as c
import requests
import os

@click.group("pipelines")
def pipelines():
    pass

@pipelines.command("list", short_help="show pipeline list")
@click.option('--format', '-f', default="json", required=False, type=click.Choice(pp.valid_formats),
              help="output format")
def list_pipelines(format):
    """
    Show pipelines list
    """
    pipelines = p.list()
    printer = pp.Printer(pipelines)
    printer.render(format=format)



@pipelines.command("add-tables", short_help="Add a table to a pipeline")
@click.option('--id', type=click.INT, required=True)
@click.option('--connector-id', type=click.INT, required=True)
@click.option('--schema', type=click.STRING, required=True)
@click.option('--tables', type=click.STRING, required=True)
@click.option('--format', '-f', default="json", required=False, type=click.Choice(pp.valid_formats),
              help="output format")
def add_tables(format, id, connector_id,  schema, tables):
    """
    Updates a pipeline and adds a table to it
    """
   
    try:
        result = p.add_tables_to_pipeline(id, connector_id, schema, tables)             
        printer = pp.Printer(result)
        printer.render(format=format)
    except requests.RequestException as e:
        print(f"Error submitting data: {e}")

@pipelines.command("add-clarity-tables", short_help="Adds multiple tables to the Clarity pipeline")
@click.option('--tables', type=click.STRING, required=True)
@click.option('--format', '-f', default="json", required=False, type=click.Choice(pp.valid_formats),
              help="output format")
def update_clarity_pipeline(format, tables):
    try:
        result = p.add_tables_to_pipeline(123, 99, "ORGFILTER", tables)             
        printer = pp.Printer(result)
        printer.render(format=format)
    except requests.RequestException as e:
        print(f"Error submitting data: {e}")


# @pipelines.group("tables", short_help="manage pipeline tables")
# def pipelines_tables():
#     pass

# def add_table_wizard(client):
#     client = client
#     user_data = {}


#     def select_pipeline():
#         result = p.list()
        
#         #map results to list of dicts containing ids and names
#         _pipelines = [{"id": r["pipelineID"], "name": r["pipelineName"]} for r in result]

#         questions = [
#             inquirer.List('choice', 
#                           message="Select your pipeline",
#                           choices=_pipelines,
#                           carousel=True),
#         ]
#         return inquirer.prompt(questions)

#     def select_source_connector():
#         result = c.list()
        
#         #map results to list of dicts containing ids and names
#         _connectors = [{"id": r["connectorID"], "name": r["connectorName"]} for r in result]

#         questions = [
#             inquirer.List('choice', 
#                           message="Select the source connector",
#                           choices=_connectors,
#                           carousel=True),
#         ]
#         return inquirer.prompt(questions)

#     def specify_tables():
#         questions = [
#             inquirer.Text('info', message="Enter the tables you want to add, separated by commas in the format <schema>.<table>"),
#         ]
#         return inquirer.prompt(questions)

#     # Step 1
#     selected_pipeline = select_pipeline()
#     user_data["pipelineID"] = selected_pipeline["choice"]["id"]

#     # Step 2 (conditional)
#     source_connector = select_source_connector()
#     source_connector_id = source_connector["choice"]["id"]
    

#     # Final Step (can add more steps similarly)
#     tables = specify_tables()

#     # Split tables by comma and convert to list
#     tables = tables["info"].split(",")

#     ingestion_type = 'snapshot'   
#     source_column_names = None
#     target_connector_id = 0 #Question: How to determine this?
#     target_schema_name = None
#     target_table_name = None
#     merge_columns = None
#     watermark_column_name = None
#     snapshot_retention_num = 3

#     user_data["items"] = []
#     #For each table in list add an object to user_data["items"]
#     for table in tables:
#         # Split the table by period, use the first part as source schema name and second part as table name
#         source_schema_name, source_table_name = table.split(".")
#         user_data["items"].append(
#             {
#           "artifactType": "database",
#           "ingestionType": ingestion_type,
#           "sourceSchemaName": source_schema_name,
#           "sourceTableName": source_table_name,
#           "sourceColumnNames": source_column_names,
#           "mergeColumns": merge_columns,
#           "targetSchemaName": target_schema_name,
#           "targetTableName": target_table_name,
#           "sourceConnectionID": source_connector_id,
#           "targetConnectionID": target_connector_id,
#           "watermarkColumnName": watermark_column_name,
#           "snapshotRetentionNum": snapshot_retention_num
#         })

#     return user_data

# @pipelines_tables.command("add", short_help="add tables to a pipeline")
# @click.option('--format', '-f', default="json", required=False, type=click.Choice(pp.valid_formats),
#               help="output format")
# def add_tables_to_pipeline_wizard( format):
#     client = api.create_client()   
#     data = add_table_wizard(client, format)
    
#     try:
#         p.modify_artifacts(data)               
#         print("Data submitted successfully!")
#     except requests.RequestException as e:
#         print(f"Error submitting data: {e}")


