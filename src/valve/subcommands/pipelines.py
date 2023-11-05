import click

import valve.core.api as api
import valve.core.auth
import valve.utils.printer as pp

@click.group("pipelines")
def pipelines():
    pass

@pipelines.command("list", short_help="show user list")
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
    pipelines = client.pipeline.list()
    printer = pp.Printer(pipelines)
    printer.render(format=format)
#    printer.render(format=format, columns=['firstName', 'lastName'])
