import click


@click.group(short_help="biodigiknow CLI.")
def biodigiknow():
    """biodigiknow CLI.
    """
    pass


@biodigiknow.command()
@click.argument("name", default="biodigiknow")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [biodigiknow]
