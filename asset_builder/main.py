"""
The main file
"""
import http
import json
import logging
import os
import pathlib
import tempfile
import webbrowser

import click

from asset_builder.data_structures.configuration import Configuration
from asset_builder.render.body_renderer import render_asset_group
from asset_builder.render.context import Context
from asset_builder.render.head_renderer import render_head
from asset_builder.render.watch_renderer import render_watch_script
from asset_builder.watch.watch_handler import WatchHandler
from asset_builder.watch.watch_server import start_server_thread

OUTPUT_FILE = pathlib.Path("build", "output.html")
TEMP_FILE = pathlib.Path(tempfile.gettempdir(), "assetBuilder", "output.html")


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


def render_html(config_file: str, output_file: str, is_watch=False):
    """
    Renders the content from the configuration
    """
    config = load_configuration(config_file)
    context = Context(**config.settings, is_watch=is_watch)

    with context.tag("html"):
        render_head(context)

        with context.tag("body"):
            render_asset_group(context, config.assets)
            render_watch_script(context)

    save_output(output_file, context.getvalue())


@click.group()
def cli():
    """
    A command line tool for creating ironsworn asset cards
    """


@cli.command()
@click.option('--verbose', '-v', is_flag=True, help='Shows errors that might occur and are ignored')
@click.argument('config_file')
def watch(config_file: str, verbose):
    """
    Watched the changes and renders them
    """
    def on_modify(*_):
        try:
            render_html(config_file, str(TEMP_FILE), is_watch=True)

        # Catching errors that might occur while trying to build
        # invalid config due to real time editing
        except json.JSONDecodeError as error:
            logging.debug(error)
        except TypeError as error:
            logging.debug(error)
        except KeyError as error:
            logging.debug(error)

    if verbose:
        logging.basicConfig(level=logging.DEBUG)

    render_html(config_file, str(TEMP_FILE), is_watch=True)
    start_server_thread()
    webbrowser.open("http://localhost:8000/output.html")
    WatchHandler(config_file, on_modify).start_watch()


@cli.command()
@click.option('--output', '-o', default=str(OUTPUT_FILE), help='Output file')
@click.argument('config_file')
def build(config_file: str, output: str):
    """
    Builds the asset cards
    """
    render_html(config_file, output)
    click.echo(f"Assets built successfully in \"{output}\"")
