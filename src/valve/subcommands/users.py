import click

import valve.utils.printer as pp

import valve.core.resources.users as u

@click.group("users")
def users():
    pass

@users.command("list", short_help="show user list")
@click.option('--format', '-f', default="json", required=False, type=click.Choice(pp.valid_formats),
              help="output format")
def list_users( format):
    """
    Show users list
    """
    result = u.list()
    printer = pp.Printer(result)
    printer.render(format=format)
#    printer.render(format=format, columns=['firstName', 'lastName'])
