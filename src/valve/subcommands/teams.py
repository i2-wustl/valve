import click

import valve.core.api as api
import valve.core.auth
import valve.utils.printer as pp

@click.group("teams")
def teams():
    pass

@teams.command("list", short_help="show teams list")
@click.option('--debug', '-d', is_flag=True, show_default=True, default=False,
              help="Print extra debugging output")
@click.option('--format', '-f', default="json", required=False, type=click.Choice(pp.valid_formats),
              help="output format")
def list_users(debug, format):
    """
    Show teams list
    """
    credentials = valve.core.auth.login(debug=debug)
    client = api.API(debug=debug, credentials=credentials)
    teams = client.teams.list()
    printer = pp.Printer(teams)
    printer.render(format=format)


@teams.group("users")
def users():
    """
    Manage team users
    """
    pass

@users.command("add", short_help="Add users to team group")
@click.argument('team_id', type=click.INT, required=True)
@click.argument('emails', type=click.STRING, required=True, short_help="Comma separated list of email addresses")
@click.option('--debug', '-d', is_flag=True, show_default=True, default=False,
              help="Print extra debugging output")
@click.option('--format', '-f', default="json", required=False, type=click.Choice(pp.valid_formats),
              help="output format")
def add_user_to_team_group( debug, format, team_id, emails):
    """
    Add users to team group
    """
    credentials = valve.core.auth.login(debug=debug)
    client = api.API(debug=debug, credentials=credentials)

    email_list = emails.split(",")
    for email in email_list:
        email = email.strip()
        user_data = client.users.get_by_email(email)
        response = client.teams.add_to_team(team_id, user_data["id"])
        printer = pp.Printer(response)
        if isinstance(response, str):
            print(response) #TODO: do this better
        else:
            printer.render(format=format)

