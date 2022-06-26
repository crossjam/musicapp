import logging
import os
import re

from pathlib import Path

from libpytunes import Library

# create exceptions for LibFileNotFound and FabricDirectoryDoesNotExist

FABRICLIVE_DIR_RGX = r"^(?P<series>(?:FABRICLIVE)) (?P<release>\d+) - (?P<artist>.+)$"
FABRICLIVE_PLAYLIST_RGX = (
    r"(?P<artist>.+): (?P<series>(?:FABRICLIVE)) (?P<release>\d+)$"
)

FABRIC_DIR_RGX = r"^(?P<series>(?:fabric[a-z]*)) (?P<release>\d+) - (?P<artist>.+)$"
FABRIC_PLAYLIST_RGX = r"(?P<artist>.+): (?P<series>(?:fabric)) (?P<release>\d+)$"


def fabric_itunes_playlists(
    itunes_lib_path="./iTunes-Library.xml", rgx_str=r"(.+): fabric (\d+)$"
):

    fabric_rgx = re.compile(rgx_str)

    res = {}

    library = Library(Path(itunes_lib_path).expanduser())

    for playlist_name in library.getPlaylistNames():
        m = fabric_rgx.search(playlist_name)
        if not m:
            continue
        series, playlist_artist, playlist_release = (
            m.group("series"),
            m.group("artist"),
            m.group("release"),
        )
        res[
            int(playlist_release)
        ] = f"{series} {int(playlist_release)} - {playlist_artist}"

    return res


def fabric_directory_folders(itunes_dir_path=".", rgx_str=r"^fabric (\d+) - (.+)$"):
    fabric_rgx = re.compile(rgx_str)

    res = {}
    for path_name in os.listdir(str(Path(itunes_dir_path).expanduser())):
        m = fabric_rgx.search(path_name)
        if not m:
            continue
        series, playlist_artist, playlist_release = (
            m.group("series"),
            m.group("artist"),
            m.group("release"),
        )
        res[
            int(playlist_release)
        ] = f"{series} {int(playlist_release)} - {playlist_artist}"

    return res


def missing_fabric_content(
    itunes_dir_path=".",
    itunes_lib_path="./iTunes-Library.xml",
    playlist_rgx_str=r"(?P<title>.+): (?P<series>(?i:fabric[a-z]*)) (?P<release>\d+)$",
    dir_rgx_str=r"^(?P<series>(?i:fabric[a-z]*)) (?P<release>\d+) - (?P<title>.+)$",
):
    logging.debug("playlist_rgx: %s, dir_rgx: %s", playlist_rgx_str, dir_rgx_str)
    itunes_lists = fabric_itunes_playlists(itunes_lib_path, playlist_rgx_str)
    dir_lists = fabric_directory_folders(itunes_dir_path, dir_rgx_str)

    missing_releases = sorted(set(dir_lists.keys()) - set(itunes_lists.keys()))

    return dict(((k, dir_lists[k]) for k in missing_releases))
