"""
A file for rendering the back of the asset
"""
from asset_builder.render.context import Context


def render_card_back(context: Context, subtitle: str):
    """
    Renders the back of the asset card
    """
    with context.tag("div", ("class", "asset-back")):
        with context.tag("div", ("class", "card-back-title")):
            context.text(context.title.upper())
        with context.tag("div", ("class", "card-back-type")):
            context.text(subtitle.upper())
