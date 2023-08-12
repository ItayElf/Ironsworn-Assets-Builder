"""
A file for rendering the back of the asset
"""
from asset_builder.render.context import Context


def render_asset_back(context: Context, asset_type: str):
    """
    Renders the back of the asset card
    """
    with context.tag("div", ("class", "asset-back")):
        with context.tag("div", ("class", "asset-back-title")):
            context.text(context.title.upper())
        with context.tag("div", ("class", "asset-back-type")):
            context.text(asset_type.upper())
