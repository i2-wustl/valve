import click

import valve.core.api as api
import valve.core.auth
import valve.utils.printer as pp

@click.group("users")
def users():
    pass

@users.command("list", short_help="show user list")
@click.option('--debug', '-d', is_flag=True, show_default=True, default=False,
              help="Print extra debugging output")
@click.option('--format', '-f', default="json", required=False, type=click.Choice(pp.valid_formats),
              help="output format")
def list_users(debug, format):
    """
    Show users list
    """
    credentials = valve.core.auth.login(debug=debug)
    client = api.API(debug=debug, credentials=credentials)
    users = client.users.list()
    printer = pp.Printer(users)
    printer.render(format=format)
#    printer.render(format=format, columns=['firstName', 'lastName'])
