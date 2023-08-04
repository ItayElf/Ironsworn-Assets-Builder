"""
A file for rendering an asset
"""

from data_structures.asset import Asset
from renderer.context import Context


def render_top_area(context: Context, asset: Asset):
    """
    Renders the top area of the asset (title, write-ins icon and description)
    """
    with context.tag("div", ("class", "top-area")):
        with context.tag("div", ("class", "asset-type")):
            context.text(asset.type)


def render_asset(context: Context, asset: Asset):
    """
    Renders an asset
    """
    with context.tag("div", ("class", "asset-background")):
        render_top_area(context, asset)
