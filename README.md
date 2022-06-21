# musicapp

[![PyPI](https://img.shields.io/pypi/v/musicapp.svg)](https://pypi.org/project/musicapp/)
[![Changelog](https://img.shields.io/github/v/release/crossjam/musicapp?include_prereleases&label=changelog)](https://github.com/crossjam/musicapp/releases)
[![Tests](https://github.com/crossjam/musicapp/workflows/Test/badge.svg)](https://github.com/crossjam/musicapp/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/crossjam/musicapp/blob/master/LICENSE)

Tools For Music.app Data

## Installation

Install this tool using `pip`:

    pip install musicapp

## Usage

For help, run:

    musicapp --help

You can also use:

    python -m musicapp --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd musicapp
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
