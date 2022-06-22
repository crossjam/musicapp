from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="musicapp",
    description="Tools For Music.app Data",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Brian M. Dennis",
    url="https://github.com/crossjam/musicapp",
    project_urls={
        "Issues": "https://github.com/crossjam/musicapp/issues",
        "CI": "https://github.com/crossjam/musicapp/actions",
        "Changelog": "https://github.com/crossjam/musicapp/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["musicapp"],
    entry_points="""
        [console_scripts]
        musicapp=musicapp.cli:cli
    """,
    install_requires=[
        "click",
        "libpytunes@git+https://github.com/anirudhra/libpytunes",
    ],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)
