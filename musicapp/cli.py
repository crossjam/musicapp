import click
from tabulate import tabulate

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
    output_table = tabulate(
        missing_fabric_content().items(), headers=["Release", "Name"]
    )

    click.echo(output_table)
