"""
A file for rendering a monster
"""

from asset_builder.data_structures.monster_card.monster_card import MonsterCard
from asset_builder.render.context import Context
from asset_builder.render.monster_renderer.monster_data_renderer import render_monster_data
from asset_builder.render.monster_renderer.monster_top_renderer import render_monster_top_area
from asset_builder.render.monster_renderer.monster_track_renderer import render_monster_number_track


def render_monster(context: Context, monster: MonsterCard):
    """
    Renders a monster
    """
    with context.tag("div", ("class", "card-background")):
        with context.tag("div"):
            render_monster_top_area(context, monster)
            render_monster_data(context, monster)
        render_monster_number_track(context)
