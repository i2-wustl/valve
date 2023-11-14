import signal

import click
from dotenv import load_dotenv

from valve.version import __version__
import valve.subcommands.users as u
import valve.subcommands.pipelines as p
import valve.subcommands.connector as c
import valve.subcommands.teams as t

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

cli.add_command(u.users)
cli.add_command(p.pipelines)
cli.add_command(c.connector)
cli.add_command(t.teams)
