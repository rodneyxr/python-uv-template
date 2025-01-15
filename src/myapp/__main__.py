import logging

import click

from myapp import logger, settings


@click.option("--debug", is_flag=True, help="Enable debug mode")
@click.group()
def cli(debug: bool):
    if debug or settings.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Debug mode enabled")


@cli.command()
@click.option("--world", is_flag=True, help="Include world in the greeting")
@click.option("--count", default=1, help="Number of greetings to print")
def hello(world: bool, count: int):
    """Sample command that prints hello (world).

    Example:
        $ myapp hello
        Hello!

        $ myapp hello --world
        Hello, world!

        $ myapp hello --world --count 3
        Hello, world!
        Hello, world!
        Hello, world!

    Args:
        world (bool): Whether to include "world" in the greeting.
        count (int): Number of greetings to print.
    """
    greeting = "Hello, world!" if world else "Hello!"
    for _ in range(count):
        click.echo(greeting)


if __name__ == "__main__":
    cli()
