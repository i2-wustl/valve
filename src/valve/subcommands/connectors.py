import click
import valve.utils.printer as pp
import valve.core.resources.connectors as c


@click.group("connectors")
def connectors():
    pass


@connectors.command("list", short_help="show user list")
@click.option(
    "--format",
    "-f",
    default="json",
    required=False,
    type=click.Choice(pp.valid_formats),
    help="output format",
)
def list_connectors(format):
    """
    Show connector list
    """
    connectors = c.list()
    printer = pp.Printer(connectors)
    printer.render(format=format)


#    printer.render(format=format, columns=['firstName', 'lastName'])


@connectors.command(
    "list-catalogs",
    short_help="list raw catalogs/schemas data associated with a connector",
)
@click.option(
    "--connector-id",
    "-c",
    type=click.INT,
    required=True,
    help="connector-id associated with the catalogs",
)
@click.option(
    "--format",
    "-f",
    default="json",
    required=False,
    type=click.Choice(pp.valid_formats),
    help="output format",
)
def list_catalogs(format, connector_id):
    """
    List raw catalog/schema data associated with connector
    """
    connectors = c.list_catalogs(connector_id)
    printer = pp.Printer(connectors)
    printer.render(format=format)



@connectors.command(
    "list-catalog-tables", short_help="list raw tables data associated with a connector"
)
@click.option(
    "--connector-id",
    "-c",
    type=click.INT,
    required=True,
    help="connector-id associated with the catalogs",
)
@click.option(
    "--schema-name",
    "-s",
    type=click.STRING,
    required=True,
    help="schema name associated with the connector id",
)
@click.option(
    "--format",
    "-f",
    default="json",
    required=False,
    type=click.Choice(pp.valid_formats),
    help="output format",
)
def list_catalog_tables(format, connector_id, schema_name):
    """
    List raw catalog tables list associated with connector
    """
    connector_tables = c.list_catalog_tables(connector_id, schema_name)
    printer = pp.Printer(connector_tables)
    printer.render(format=format)


@connectors.command("describe", short_help="describe a specific connector")
@click.option(
    "--format",
    "-f",
    default="json",
    required=False,
    type=click.Choice(pp.valid_formats),
    help="output format",
)
@click.argument("connector-id", type=click.INT, required=True)
def describe(format, connector_id):
    """
    Show catalog/schemas associated with connector
    """
    rawdata = c.get(connector_id)
    printer = pp.Printer(rawdata)
    printer.render(format=format)


@connectors.command(
    "schemas", short_help="show catalogs/schemas associated with a connector"
)
@click.option(
    "--connector-id",
    "-c",
    type=click.INT,
    required=True,
    help="connector-id associated with the catalogs",
)
@click.option(
    "--format",
    "-f",
    default="json",
    required=False,
    type=click.Choice(pp.valid_formats),
    help="output format",
)
def schemas(format, connector_id):
    """
    Show catalog/schemas associated with connector
    """
    rawdata = c.list_catalogs(connector_id)
    tables = sorted(rawdata["objects"])
    connector_name = rawdata["connectorName"]
    printer = pp.Printer({connector_name: tables})
    printer.render(format=format)


@connectors.command("tables", short_help="show tables associated with a connector")
@click.option(
    "--connector-id",
    "-c",
    type=click.INT,
    required=True,
    help="connector-id associated with the catalogs",
)
@click.option(
    "--schema-name",
    "-s",
    type=click.STRING,
    required=True,
    help="schema name associated with the connector id",
)
@click.option(
    "--format",
    "-f",
    default="json",
    required=False,
    type=click.Choice(pp.valid_formats),
    help="output format",
)
def tables(format, connector_id, schema_name):
    """
    Show tables associated with connector
    """
    rawdata = c.list_catalog_tables(connector_id, schema_name)
    tables = sorted(rawdata["objects"])
    connector_name = rawdata["connectorName"]
    printer = pp.Printer({connector_name: tables})
    printer.render(format=format)
