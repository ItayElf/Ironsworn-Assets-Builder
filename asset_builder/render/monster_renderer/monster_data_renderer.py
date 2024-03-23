"""
A file for rendering the monster data
"""

from typing import List

from asset_builder.data_structures.monster_card.monster_card import MonsterCard
from asset_builder.render.context import Context


def _render_list(context: Context, title: str, fields: List[str]):
    """
    Renders a list separated by "\u2022" (bullets)
    """
    with context.tag("div", ("class", "monster-list")):
        with context.tag("span", ("class", "monster-list-title")):
            context.text(title + ": ")
        context.text(" \u2022 ".join(fields))


def _render_quest_starter(context: Context, monster: MonsterCard):
    """
    Renders the quest starter
    """
    if monster.quest_starter:
        with context.tag("div", ("class", "monster-quest-starter")):
            context.text("Quest Starter: " + monster.quest_starter)


def render_monster_data(context: Context, monster: MonsterCard):
    """
    Renders all the monster data
    """
    with context.tag("div", ("class", "monster-data")):
        _render_list(context, "Features", monster.features)
        _render_list(context, "Drives", monster.drives)
        _render_list(context, "Tactics", monster.tactics)
        if monster.terrain:
            _render_list(context, "Terrain", monster.terrain)

        _render_quest_starter(context, monster)
