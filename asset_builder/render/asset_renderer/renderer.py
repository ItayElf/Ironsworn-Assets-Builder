"""
A file for rendering an asset
"""

from asset_builder.data_structures.asset import Asset
from asset_builder.render.asset_renderer.asset_abilities_renderer import render_asset_abilities
from asset_builder.render.asset_renderer.asset_top_renderer import render_top_area
from asset_builder.render.asset_renderer.asset_track_renderer import render_asset_track
from asset_builder.render.context import Context


def render_asset(context: Context, asset: Asset):
    """
    Renders an asset
    """
    with context.tag("div", ("class", "asset-background")):
        with context.tag("div"):
            render_top_area(context, asset)
            render_asset_abilities(context, asset)
        render_asset_track(context, asset)
