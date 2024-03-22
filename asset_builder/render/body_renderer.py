"""
A file to render the body of the page
"""

from typing import List
from asset_builder.data_structures.card import Card

from asset_builder.render.asset_renderer.asset_back_renderer import render_asset_back
from asset_builder.render.context import Context


def render_card_group(context: Context, cards: List[Card]):
    """
    Renders a list of assets on a grid
    """
    with context.tag("div", ("class", "cards-group")):
        for card in cards:
            card.render(context)
        for asset_type in set(card.type for card in cards):
            render_asset_back(context, asset_type)
