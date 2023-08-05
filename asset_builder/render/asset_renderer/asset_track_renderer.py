"""
A file for rendering the asset track
"""
from typing import List
from asset_builder.data_structures.asset import Asset
from asset_builder.render.context import Context


def render_asset_number_track(context: Context, max_value: int):
    """
    Renders a number track
    """
    values = list(range(max_value+1))
    while len(values) < 6:
        values.append(-1)

    with context.tag("div", ("class", "asset-track")):
        for value in values:
            classname = f"asset-track-value asset-track-{'number' if value >= 0 else 'empty'}"
            with context.tag("div", ("class", classname)):
                if value == 0:
                    context.text("0")
                elif value > 0:
                    context.text(f"+{value}")


def render_asset_values_track(context: Context, values: List[str]):
    """
    Renders a value track
    """
    with context.tag("div", ("class", "asset-track")):
        for value in values:
            with context.tag("div", ("class", "asset-track-value asset-track-text")):
                context.text(value)


def render_asset_track(context: Context, asset: Asset):
    """
    Renders the asset track, if has any
    """
    if isinstance(asset.track, int):
        return render_asset_number_track(context, asset.track)
    elif isinstance(asset.track, list):
        return render_asset_values_track(context, asset.track)

    raise ValueError(f"Invalid value for track: {repr(asset.track)}")
