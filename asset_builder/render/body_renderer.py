"""
A file to render the body of the page
"""

from typing import List
from asset_builder.data_structures.card import Card

from asset_builder.render.context import Context


def render_card_group(context: Context, cards: List[Card]):
    """
    Renders a list of cards on a grid
    """
    with context.tag("div", ("class", "cards-group")):
        for card in cards:
            card.render(context)
        for card in {card.card_back_hash: card for card in cards}.values():
            card.render_back(context)
