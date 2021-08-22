import click
import logging
from rich.logging import RichHandler


def setup_logging():

    FORMAT = "%(message)s"
    logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt="[%X]", handlers=[RichHandler()])


@click.group(help="Default")
def main():
    setup_logging()
