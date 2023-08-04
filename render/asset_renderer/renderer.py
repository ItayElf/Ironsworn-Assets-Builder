"""
A file for rendering an asset
"""

from data_structures.asset import Asset
from render.asset_renderer.asset_abilities_renderer import render_asset_abilities
from render.asset_renderer.asset_top_renderer import render_top_area
from render.context import Context


def render_asset(context: Context, asset: Asset):
    """
    Renders an asset
    """
    with context.tag("div", ("class", "asset-background")):
        render_top_area(context, asset)
        render_asset_abilities(context, asset)
