"""
A file for rendering the top of the asset
"""
import markdown
from asset_builder.data_structures.asset_card.asset import AssetCard
from asset_builder.render.context import Context


def _render_write_in(context: Context, write_in: str):
    """
    Renders an asset write_in
    """
    with context.tag("div", ("class", "asset-write-in")):
        context.text(write_in, ":")


def _render_write_ins(context: Context, asset: AssetCard):
    """
    Renders the write ins of the asset if any
    """
    if asset.write_ins:
        for write_in in asset.write_ins:
            _render_write_in(context, write_in)


def _render_asset_description(context: Context, asset: AssetCard):
    """
    Renders the asset description if any
    """
    if asset.description:
        with context.tag("div", ("class", "asset-description")):
            context.asis(markdown.markdown(asset.description))


def _render_top_panel(context: Context, asset: AssetCard):
    """
    Renders the write-ins and description if there are any
    """
    if asset.write_ins or asset.description:
        with context.tag("div", ("class", "asset-write_ins")):
            _render_write_ins(context, asset)
            _render_asset_description(context, asset)


def _render_asset_icon(context: Context, asset: AssetCard):
    """
    Renders the asset icon, if it has one
    """
    if asset.icon_path:
        with context.tag("div", style="position: relative;"):
            with context.tag("div", ("class", "asset-icon")):
                with context.tag("img", src=asset.icon_path):
                    pass


def render_asset_top_area(context: Context, asset: AssetCard):
    """
    Renders the top area of the asset (title, write-ins icon and description)
    """
    with context.tag("div", ("class", "top-area")):
        with context.tag("div", ("class", "asset-type")):
            context.text(asset.type)
        with context.tag("div", ("class", "asset-name")):
            context.text(asset.name)

        _render_asset_icon(context, asset)
        _render_top_panel(context, asset)
