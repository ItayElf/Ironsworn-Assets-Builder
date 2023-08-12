"""
A file to render the body of the page
"""

from typing import List

from asset_builder.data_structures.asset import Asset
from asset_builder.render.asset_renderer.asset_back_renderer import \
    render_asset_back
from asset_builder.render.asset_renderer.renderer import render_asset
from asset_builder.render.context import Context


def render_asset_group(context: Context, assets: List[Asset]):
    """
    Renders a list of assets on a grid
    """
    with context.tag("div", ("class", "assets-group")):
        for asset in assets:
            render_asset(context, asset)
        for asset_type in set(asset.type for asset in assets):
            render_asset_back(context, asset_type)
