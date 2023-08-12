"""
A file to add js script to reload website
"""

import pathlib
from asset_builder.render.context import Context

JS_SCRIPT = (pathlib.Path(__file__).parent / ".." / "static" /
             "reload.js").read_text(encoding="utf-8")


def render_watch_script(context: Context):
    """
    Renders js script is watch is active
    """
    with context.tag("script"):
        context.asis(JS_SCRIPT)
