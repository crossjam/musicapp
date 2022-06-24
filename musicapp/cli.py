import click

from .fabric import missing_fabric_content


@click.group()
@click.version_option()
def cli():
    "Tools For Music.app Data"


@cli.group("fabric")
def fabric():
    pass


@fabric.command(name="missing")
def missing_fabric():
    for k, v in missing_fabric_content().items():
        click.echo(f"{k}: {v}")
