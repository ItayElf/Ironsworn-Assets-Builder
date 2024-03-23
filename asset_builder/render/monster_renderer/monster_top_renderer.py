"""
A file for rendering the top of the monster card
"""

import markdown
from asset_builder.data_structures.monster_card.monster_card import MonsterCard
from asset_builder.render.context import Context


def _render_monster_icon(context: Context, monster: MonsterCard):
    """
    Renders the asset icon, if it has one
    """
    if monster.icon_path:
        with context.tag("div", style="position: relative;"):
            with context.tag("div", ("class", "asset-icon")):
                with context.tag("img", src=monster.icon_path):
                    pass


def _render_monster_description(context: Context, monster: MonsterCard):
    """
    Renders the asset description if any
    """
    if monster.description:
        with context.tag("div", ("class", "asset-write_ins")):
            with context.tag("div", ("class", "asset-description")):
                context.asis(markdown.markdown(monster.description))


def render_monster_top_area(context: Context, monster: MonsterCard):
    """
    Renders the top area of the monster card
    """
    with context.tag("div", ("class", "top-area")):
        with context.tag("div", ("class", "asset-type")):
            if context.is_rtl:
                context.text(f"{monster.type} {monster.rank}")
            else:
                context.text(f"{monster.rank} {monster.type}")
        with context.tag("div", ("class", "asset-name")):
            context.text(monster.name)

    _render_monster_icon(context, monster)
    _render_monster_description(context, monster)
