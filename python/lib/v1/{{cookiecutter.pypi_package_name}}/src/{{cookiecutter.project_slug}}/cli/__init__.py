from argparse import ArgumentParser, Namespace
from importlib import metadata
from types import ModuleType
from typing import List


COMMANDS = []


def commands() -> List[ModuleType]:
    return sorted(COMMANDS, key=lambda x: x.__name__)


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"{{ cookiecutter.pypi_package_name }} - v{metadata.version('{{ cookiecutter.pypi_package_name }}')}",
    )

    subparsers = parser.add_subparsers(dest="command")
    subparsers.required = True

    for command in commands():
        command.configure_parser(subparsers)

    return parser.parse_args()
