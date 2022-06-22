import os
import re

from pathlib import Path

from libpytunes import Library


def itunes_fabric_playlists(itunes_lib_path="./iTunes-Library.xml"):

    fabric_rgx = re.compile(r"(.+): fabric (\d+)$")

    res = {}

    library = Library(Path(itunes_lib_path).expanduser())

    for playlist_name in library.getPlaylistNames():
        m = fabric_rgx.search(playlist_name)
        if not m:
            continue
        playlist_artist, playlist_num = m.groups()
        res[int(playlist_num)] = f"fabric {int(playlist_num)} - {playlist_artist}"

    return res


def directory_fabric_playlists(itunes_dir_path="."):
    fabric_rgx = re.compile(r"^fabric (\d+) - (.+)$")

    res = {}
    for path_name in os.listdir(str(Path(itunes_dir_path).expanduser())):
        m = fabric_rgx.search(path_name)
        if not m:
            continue
        playlist_num, playlist_artist = m.groups()
        res[int(playlist_num)] = f"fabric {int(playlist_num)} - {playlist_artist}"

    return res
