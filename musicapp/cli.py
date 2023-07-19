import csv
import json
import logging
import sys

import click
from tabulate import tabulate

from .fabric import (
    missing_fabric_content,
    FABRICLIVE_DIR_RGX,
    FABRICLIVE_PLAYLIST_RGX,
    FABRIC_DIR_RGX,
    FABRIC_PLAYLIST_RGX,
)
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
@click.pass_context
def missing_fabric(ctx, tablefmt):
    logging.debug("tablefmt: %s", tablefmt)
    logging.debug("params: %s", ctx.params)
    logging.debug("parent params: %s", ctx.parent.params)

    if ctx.parent.params.get("fabriclive", False):
        dir_rgx_str = FABRICLIVE_DIR_RGX
        playlist_rgx_str = FABRICLIVE_PLAYLIST_RGX
    else:
        dir_rgx_str = FABRIC_DIR_RGX
        playlist_rgx_str = FABRIC_PLAYLIST_RGX

    if tablefmt == "json":
        rows = [
            {"release": num, "series": series, "title": title}
            for (series, num), title in missing_fabric_content(
                playlist_rgx_str=playlist_rgx_str, dir_rgx_str=dir_rgx_str
            ).items()
        ]
        for row in rows:
            json.dump(row, sys.stdout)
            print()
    elif tablefmt == "csv":
        writer = csv.writer(sys.stdout)
        writer.writerow(["series", "release", "title"])
        for (series, release), title in missing_fabric_content(
            playlist_rgx_str=playlist_rgx_str, dir_rgx_str=dir_rgx_str
        ).items():
            writer.writerow([series, release, title])
    else:
        output_table = tabulate(
            missing_fabric_content(
                playlist_rgx_str=playlist_rgx_str, dir_rgx_str=dir_rgx_str
            ).items(),
            headers=["Release", "Title"],
            tablefmt=tablefmt,
        )
        click.echo(output_table)
