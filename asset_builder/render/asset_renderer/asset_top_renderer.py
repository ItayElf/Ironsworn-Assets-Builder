"""
A file for rendering the top of the asset
"""
from asset_builder.data_structures.asset import Asset
from asset_builder.render.context import Context


def render_write_in(context: Context, write_in: str):
    """
    Renders an asset write_in
    """
    with context.tag("div", ("class", "asset-write-in")):
        context.text(write_in, ":")


def render_write_ins(context: Context, asset: Asset):
    """
    Renders the write ins of the asset if any
    """
    if asset.write_ins:
        for write_in in asset.write_ins:
            render_write_in(context, write_in)


def render_asset_description(context: Context, asset: Asset):
    """
    Renders the asset description if any
    """
    if asset.description:
        with context.tag("div", ("class", "asset-description")):
            context.text(asset.description)


def render_top_panel(context: Context, asset: Asset):
    """
    Renders the write-ins and description if there are any
    """
    if asset.write_ins or asset.description:
        with context.tag("div", ("class", "asset-write_ins")):
            render_write_ins(context, asset)
            render_asset_description(context, asset)


def render_asset_icon(context: Context, asset: Asset):
    """
    Renders the asset icon, if it has one
    """
    if asset.icon_path:
        with context.tag("div", style="position: relative;"):
            with context.tag("div", ("class", "asset-icon")):
                with context.tag("img", src=asset.icon_path):
                    pass


def render_top_area(context: Context, asset: Asset):
    """
    Renders the top area of the asset (title, write-ins icon and description)
    """
    with context.tag("div", ("class", "top-area")):
        with context.tag("div", ("class", "asset-type")):
            context.text(asset.type)
        with context.tag("div", ("class", "asset-name")):
            context.text(asset.name)

        render_asset_icon(context, asset)
        render_top_panel(context, asset)
