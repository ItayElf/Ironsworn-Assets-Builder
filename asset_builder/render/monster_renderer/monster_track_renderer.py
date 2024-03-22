"""
A file for rendering the track for the monster
"""

from asset_builder.render.context import Context


def render_monster_number_track(context: Context):
    """
    Renders the monster track
    """
    with context.tag("div", ("class", "asset-track")):
        for value in range(1, 11):
            classname = f"asset-track-value asset-track-{
                'number' if value >= 0 else 'empty'}"
            with context.tag("div", ("class", classname)):
                context.text(str(value))
