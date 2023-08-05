"""
The main file
"""
import json
import pathlib
import tempfile

import click
import webbrowser

from asset_builder.data_structures.configuration import Configuration
from asset_builder.render.body_renderer import render_asset_group
from asset_builder.render.context import Context
from asset_builder.render.head_renderer import render_head
from asset_builder.watch_handler import WatchHandler

OUTPUT_FILE = pathlib.Path("build", "output.html")
TEMP_FILE = pathlib.Path(tempfile.gettempdir(), "output.html")


def load_configuration(filename: str) -> Configuration:
    """
    Returns a configuration object from a file
    """
    data = json.loads(pathlib.Path(filename).read_text(encoding="utf-8"))
    return Configuration.from_json(data)


def save_output(filename: str, content: str):
    """
    Saves the output to the output file
    """
    file = pathlib.Path(filename)
    file.parent.mkdir(parents=True, exist_ok=True)
    file.touch(exist_ok=True)
    file.write_text(content, encoding="utf-8")


def render_html(config_file: str, output_file: str):
    """
    Renders the content from the configuration
    """
    config = load_configuration(config_file)
    context = Context(**config.settings, is_watch=True)

    with context.tag("html"):
        render_head(context)

        with context.tag("body"):
            render_asset_group(context, config.assets)

    save_output(output_file, context.getvalue())


@click.group()
def cli():
    """
    A command line tool for creating ironsworn asset cards
    """


@cli.command()
@click.argument('config_file')
def watch(config_file: str):
    """
    Watched the changes and renders them
    """
    render_html(config_file, str(TEMP_FILE))
    webbrowser.open(str(TEMP_FILE.absolute()))
    WatchHandler(
        config_file,
        lambda _: render_html(config_file, str(TEMP_FILE))
    ).start_watch()


@cli.command()
@click.option('--output', '-o', default=str(OUTPUT_FILE), help='Output file')
@click.argument('config_file')
def build(config_file: str, output: str):
    """
    Builds the asset cards
    """
    render_html(config_file, output)
    click.echo(f"Assets built successfully in \"{output}\"")
