"""
A file for rendering a monster
"""

from asset_builder.data_structures.monster_card.monster_card import MonsterCard
from asset_builder.render.context import Context
from asset_builder.render.monster_renderer.monster_track_renderer import render_monster_number_track


def render_monster(context: Context, monster: MonsterCard):
    """
    Renders a monster
    """
    with context.tag("div", ("class", "card-background")):
        with context.tag("div"):
            pass
        render_monster_number_track(context)
