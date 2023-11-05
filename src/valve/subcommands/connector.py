import click

import valve.core.api as api
import valve.core.auth
import valve.utils.printer as pp

@click.group("connector")
def connector():
    pass

@connector.command("list", short_help="show user list")
@click.option('--debug', '-d', is_flag=True, show_default=True, default=False,
              help="Print extra debugging output")
@click.option('--format', '-f', default="json", required=False, type=click.Choice(pp.valid_formats),
              help="output format")
def list_connectors(debug, format):
    """
    Show connector list
    """
    credentials = valve.core.auth.login(debug=debug)
    client = api.API(debug=debug, credentials=credentials)
    connectors = client.connector.list()
    printer = pp.Printer(connectors)
    printer.render(format=format)
#    printer.render(format=format, columns=['firstName', 'lastName'])

@connector.command("list-catalogs", short_help="list raw catalogs/schemas data associated with a connector")
@click.option('--connector-id', '-c', type=click.INT, required=True,
              help="connector-id associated with the catalogs")
@click.option('--debug', '-d', is_flag=True, show_default=True, default=False,
              help="Print extra debugging output")
@click.option('--format', '-f', default="json", required=False, type=click.Choice(pp.valid_formats),
              help="output format")
def list_catalogs(debug, format, connector_id):
    """
    List raw catalog/schema data associated with connector
    """
    credentials = valve.core.auth.login(debug=debug)
    client = api.API(debug=debug, credentials=credentials)
    connectors = client.connector.list_catalogs(connector_id)
    printer = pp.Printer(connectors)
    printer.render(format=format)
#    printer.render(format=format, columns=['firstName', 'lastName'])

@connector.command("list-catalog-tables", short_help="list raw tables data associated with a connector")
@click.option('--connector-id', '-c', type=click.INT, required=True,
              help="connector-id associated with the catalogs")
@click.option('--debug', '-d', is_flag=True, show_default=True, default=False,
              help="Print extra debugging output")
@click.option('--format', '-f', default="json", required=False, type=click.Choice(pp.valid_formats),
              help="output format")
def list_catalog_tables(debug, format, connector_id):
    """
    List raw catalog tables list associated with connector
    """
    credentials = valve.core.auth.login(debug=debug)
    client = api.API(debug=debug, credentials=credentials)
    connector_tables = client.connector.list_catalog_tables(connector_id)
    printer = pp.Printer(connector_tables)
    printer.render(format=format)

@connector.command("describe", short_help="describe a specific connector")
@click.option('--debug', '-d', is_flag=True, show_default=True, default=False,
              help="Print extra debugging output")
@click.option('--format', '-f', default="json", required=False, type=click.Choice(pp.valid_formats),
              help="output format")
@click.argument('connector-id', type=click.INT, required=True)
def describe(debug, format, connector_id):
    """
    Show catalog/schemas associated with connector
    """
    credentials = valve.core.auth.login(debug=debug)
    client = api.API(debug=debug, credentials=credentials)
    rawdata = client.connector.get(connector_id)
    printer = pp.Printer(rawdata)
    printer.render(format=format)

@connector.command("schemas", short_help="show catalogs/schemas associated with a connector")
@click.option('--connector-id', '-c', type=click.INT, required=True,
              help="connector-id associated with the catalogs")
@click.option('--debug', '-d', is_flag=True, show_default=True, default=False,
              help="Print extra debugging output")
@click.option('--format', '-f', default="json", required=False, type=click.Choice(pp.valid_formats),
              help="output format")
def schemas(debug, format, connector_id):
    """
    Show catalog/schemas associated with connector
    """
    credentials = valve.core.auth.login(debug=debug)
    client = api.API(debug=debug, credentials=credentials)
    rawdata = client.connector.list_catalogs(connector_id)
    tables = sorted(rawdata['objects'])
    connector_name = rawdata['connectorName']
    printer = pp.Printer({connector_name: tables})
    printer.render(format=format)
#    printer.render(format=format, columns=['firstName', 'lastName'])

@connector.command("tables", short_help="show tables associated with a connector")
@click.option('--connector-id', '-c', type=click.INT, required=True,
              help="connector-id associated with the catalogs")
@click.option('--debug', '-d', is_flag=True, show_default=True, default=False,
              help="Print extra debugging output")
@click.option('--format', '-f', default="json", required=False, type=click.Choice(pp.valid_formats),
              help="output format")
def tables(debug, format, connector_id):
    """
    Show tables associated with connector
    """
    credentials = valve.core.auth.login(debug=debug)
    client = api.API(debug=debug, credentials=credentials)
    rawdata = client.connector.list_catalog_tables(connector_id)
    tables = sorted(rawdata['objects'])
    connector_name = rawdata['connectorName']
    printer = pp.Printer({connector_name: tables})
    printer.render(format=format)
