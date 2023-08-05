"""
A file to render the body of the page
"""

from typing import List
from data_structures.asset import Asset
from render.asset_renderer.renderer import render_asset
from render.context import Context


def render_asset_group(context: Context, assets: List[Asset]):
    """
    Renders a list of assets on a grid
    """
    with context.tag("div", ("class", "assets-group")):
        for asset in assets:
            render_asset(context, asset)
