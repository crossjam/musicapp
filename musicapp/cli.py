import click

from .fabric import missing_fabric_content


@click.group()
@click.version_option()
def cli():
    "Tools For Music.app Data"


@cli.command(name="missing-fabric")
def missing_fabric():
    print(missing_fabric_content())
