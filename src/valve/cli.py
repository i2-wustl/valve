import signal
import click
import valve.core.api as api

import valve.core.auth
from pprint import pprint
from valve.version import __version__
from dotenv import load_dotenv

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

@click.option('--debug', '-d', is_flag=True, show_default=True, default=False, required=True, help="Print extra debugging output")
def list_users(debug):
    credentials = valve.core.auth.login()
    client = api.API(debug=debug, credentials=credentials)
    users = client.users.list()
    pprint(users)
