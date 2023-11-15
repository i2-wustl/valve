import click
import valve.utils.printer as pp
import valve.core.resources.teams as t

@click.group("teams")
def teams():
    pass


@teams.command("list", short_help="show teams list")
@click.option(
    "--format",
    "-f",
    default="json",
    required=False,
    type=click.Choice(pp.valid_formats),
    help="output format",
)
def list_teams(format):
    """
    Show teams list
    """

    teams = t.list_teams()
    printer = pp.Printer(teams)
    printer.render(format=format)


@teams.group("users")
def users():
    """
    Manage team users
    """
    pass


@users.command("add", short_help="Add users to team group")
@click.argument("team_id", type=click.INT, required=True)
@click.argument("emails", type=click.STRING, required=True)
@click.option(
    "--format",
    "-f",
    default="json",
    required=False,
    type=click.Choice(pp.valid_formats),
    help="output format",
)
def add_users_to_team_group(format, team_id, emails):
    """
    Add users to team group
    """

    email_list = emails.split(",")
    responses = [t.add_to_team(e, team_id) for e in email_list]
    printer = pp.Printer(responses)
    printer.render(format=format)


@users.command("remove", short_help="Remove users from team group")
@click.argument("team_id", type=click.INT, required=True)
@click.argument(
    "emails",
    type=click.STRING,
    required=True
)
@click.option(
    "--format",
    "-f",
    default="json",
    required=False,
    type=click.Choice(pp.valid_formats),
    help="output format",
)
def remove_users_from_team_group( format, team_id, emails):
    """
    Remove users to team group
    """
    email_list = emails.split(",")
    responses = [t.remove_from_team(e, team_id) for e in email_list]
    printer = pp.Printer(responses)
    printer.render(format=format)
    
