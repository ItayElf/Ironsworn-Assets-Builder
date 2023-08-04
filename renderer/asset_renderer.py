"""
A file for rendering an asset
"""

from data_structures.asset import Asset
from renderer.context import Context


def render_write_in(context: Context, write_in: str):
    """
    Renders an asset write_in
    """
    with context.tag("div", ("class", "asset-write-in")):
        context.text(write_in + ":")


def render_top_area(context: Context, asset: Asset):
    """
    Renders the top area of the asset (title, write-ins icon and description)
    """
    with context.tag("div", ("class", "top-area")):
        with context.tag("div", ("class", "asset-type")):
            context.text(asset.type)
        with context.tag("div", ("class", "asset-name")):
            context.text(asset.name)

        if asset.icon_path:
            with context.tag("div", style="position: relative;"):
                with context.tag("div", ("class", "asset-icon")):
                    with context.tag("img", src=asset.icon_path):
                        pass

        if asset.write_ins:
            with context.tag("div", ("class", "asset-write_ins")):
                for write_in in asset.write_ins:
                    render_write_in(context, write_in)


def render_asset(context: Context, asset: Asset):
    """
    Renders an asset
    """
    with context.tag("div", ("class", "asset-background")):
        render_top_area(context, asset)
