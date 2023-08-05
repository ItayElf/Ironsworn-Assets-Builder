"""
A file that renders the head of the html
"""
import pathlib
from asset_builder.render.context import Context

FILE_LOCATION = pathlib.Path(__file__).parent
BASE_CSS = pathlib.Path(
    FILE_LOCATION,
    "..",
    "static",
    "base.css"
).read_text(encoding="utf-8").replace("\n", "")


def add_styles(context: Context):
    """
    Adds css to the context
    """
    with context.tag("style"):
        context.text(BASE_CSS)


def render_head(context: Context):
    """
    Renders the head tag
    """
    with context.tag("head"):
        add_styles(context)
