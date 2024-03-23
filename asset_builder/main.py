"""
The main file
"""
import json
import logging
import pathlib
import tempfile
import webbrowser
import yaml

import click

from asset_builder.data_structures.configuration import Configuration
from asset_builder.render.body_renderer import render_card_group
from asset_builder.render.context import Context
from asset_builder.render.head_renderer import render_head
from asset_builder.render.images_renderer import render_images
from asset_builder.render.pdf_renderer import render_pdf
from asset_builder.render.watch_renderer import render_watch_script
from asset_builder.watch.watch_handler import WatchHandler
from asset_builder.watch.watch_server import start_server_thread

HTML_OUTPUT_FILE = pathlib.Path("build", "output.html")
HTML_TEMP_FILE = pathlib.Path(
    tempfile.gettempdir(), "assetBuilder", "output.html")
PNG_OUTPUT_DIR = pathlib.Path("build", "assets")
PNG_TEMP_DIR = pathlib.Path(tempfile.gettempdir(), "assetBuilder", "assets")
PDF_OUTPUT_FILE = pathlib.Path("build", "output.pdf")


def load_configuration(filename: str) -> Configuration:
    """
    Returns a configuration object from a file
    """
    path = pathlib.Path(filename)
    content = path.read_text(encoding="utf-8")
    if path.suffix == ".json":
        data = json.loads(content)
    elif path.suffix == ".yaml" or path.suffix == ".yml":
        data = yaml.load(path.open(encoding="utf-8"), yaml.FullLoader)
    return Configuration.from_json(data)


def get_output_file(file_type: str):
    """
    Returns the default output file
    """
    if file_type == "html":
        return str(HTML_OUTPUT_FILE)
    if file_type == "png":
        return str(PNG_OUTPUT_DIR)
    if file_type == "pdf":
        return str(PDF_OUTPUT_FILE)

    raise ValueError(f"No default file for type {file_type}")


def save_output(filename: str, content: str):
    """
    Saves the output to the output file
    """
    file = pathlib.Path(filename)
    file.parent.mkdir(parents=True, exist_ok=True)
    file.touch(exist_ok=True)
    file.write_text(content, encoding="utf-8")


def render_html(config: Configuration, output_file: str, is_watch=False):
    """
    Renders the content from the configuration
    """
    context = Context(**config.settings, is_watch=is_watch)

    with context.tag("html"):
        render_head(context)

        with context.tag("body"):
            render_card_group(context, config.cards)
            if context.is_watch:
                render_watch_script(context)

    save_output(output_file, context.getvalue())


@click.group()
def cli():
    """
    A command line tool for creating ironsworn asset cards
    """


@cli.command()
@click.option('--verbose', '-v', is_flag=True, help='Shows errors that might occur and are ignored')
@click.option('--no-new-window', '-N', is_flag=True, help='Do not open a new browser, use an existing one')
@click.argument('config_file')
def watch(config_file: str, verbose: bool, no_new_window: bool):
    """
    Watched the changes and renders them
    """
    config = load_configuration(config_file)

    def on_modify(*_):
        try:
            config = load_configuration(config_file)
            render_html(config, str(HTML_TEMP_FILE), is_watch=True)

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

    render_html(config, str(HTML_TEMP_FILE), is_watch=True)
    start_server_thread()
    if not no_new_window:
        webbrowser.open("http://localhost:8000/output.html")
    WatchHandler(config_file, on_modify).start_watch()


@cli.command()
@click.option('--output', '-o', default="", help='Output file (output directory for png)')
@click.option("--file-type", "-t", default="html", type=click.Choice(["html", "png", "pdf"], case_sensitive=False))
@click.argument('config_file')
def build(config_file: str, output: str, file_type: str):
    """
    Builds the asset cards
    """
    config = load_configuration(config_file)
    if not output:
        output = get_output_file(file_type)

    if file_type == "html":
        render_html(config, output)
    elif file_type == "png":
        render_images(config, output)
    elif file_type == "pdf":
        render_images(config, str(PNG_TEMP_DIR))
        save_output(output, "")
        render_pdf(config, str(PNG_TEMP_DIR), output)

    click.echo(f"Assets built successfully in \"{output}\"")


if __name__ == "__main__":
    cli()
