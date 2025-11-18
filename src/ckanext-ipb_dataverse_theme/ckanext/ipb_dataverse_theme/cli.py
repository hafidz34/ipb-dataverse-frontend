import click


@click.group(short_help="ipb_dataverse_theme CLI.")
def ipb_dataverse_theme():
    """ipb_dataverse_theme CLI.
    """
    pass


@ipb_dataverse_theme.command()
@click.argument("name", default="ipb_dataverse_theme")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [ipb_dataverse_theme]
