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
def list_pipelines(debug, format):
    """
    Show connector list
    """
    credentials = valve.core.auth.login(debug=debug)
    client = api.API(debug=debug, credentials=credentials)
    connectors = client.connector.list()
    printer = pp.Printer(connectors)
    printer.render(format=format)
#    printer.render(format=format, columns=['firstName', 'lastName'])

@connector.command("list-catalogs", short_help="show user list")
@click.option( '--connector-id', '-c', type=click.INT, required=True,
              help="connector-id associated with the catalogs")
@click.option('--debug', '-d', is_flag=True, show_default=True, default=False,
              help="Print extra debugging output")
@click.option('--format', '-f', default="json", required=False, type=click.Choice(pp.valid_formats),
              help="output format")
def list_catalogs(debug, format, connector_id):
    """
    Show catalog list associated with connector
    """
    credentials = valve.core.auth.login(debug=debug)
    client = api.API(debug=debug, credentials=credentials)
    connectors = client.connector.list_catalog(connector_id)
    printer = pp.Printer(connectors)
    printer.render(format=format)
#    printer.render(format=format, columns=['firstName', 'lastName'])
