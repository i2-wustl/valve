import signal

import click
from dotenv import load_dotenv

from valve.version import __version__
import valve.core.api as api
import valve.core.auth
import valve.utils.printer as pp

# Load environment variables from .env file
load_dotenv()

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__version__)
def cli():
    '''A collection of related tools for handling data lake administration.'''
    # to make this script/module behave nicely with unix pipes
    # http://newbebweb.blogspot.com/2012/02/python-head-ioerror-errno-32-broken.html
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)

@cli.group("users")
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
