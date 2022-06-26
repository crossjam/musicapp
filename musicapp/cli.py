import csv
import json
import logging
import sys

import click
from tabulate import tabulate

from .fabric import missing_fabric_content
from .logconfig import DEFAULT_LOG_FORMAT, logging_config


pass_dict = click.make_pass_decorator(dict)


@click.group()
@click.version_option()
@click.option(
    "--log-format",
    type=click.STRING,
    default=DEFAULT_LOG_FORMAT,
    help="Python logging format string",
)
@click.option(
    "--log-level", default="ERROR", help="Python logging level", show_default=True
)
@click.option(
    "--log-file",
    help="Python log output file",
    type=click.Path(dir_okay=False, writable=True, resolve_path=True),
    default=None,
)
def cli(log_format, log_level, log_file):
    "Tools For Music.app Data"
    logging_config(log_format, log_level, log_file)


@cli.group("fabric")
@click.option(
    "+live/-live", "fabriclive", help="Query FabricLive releases", default=False
)
def fabric(fabriclive):
    pass


@fabric.command(name="missing")
@click.option("--fmt", "tablefmt", help="Table format", default="simple")
def missing_fabric(tablefmt):
    logging.debug("tablefmt: %s", tablefmt)

    if tablefmt == "json":
        rows = [{"release": k, "title": v} for k, v in missing_fabric_content().items()]
        for row in rows:
            json.dump(row, sys.stdout)
            print()
    elif tablefmt == "csv":
        writer = csv.writer(sys.stdout)
        writer.writerow(["release", "title"])
        for k, v in missing_fabric_content().items():
            writer.writerow([k, v])
    else:
        output_table = tabulate(
            missing_fabric_content().items(),
            headers=["Release", "Title"],
            tablefmt=tablefmt,
        )
        click.echo(output_table)
