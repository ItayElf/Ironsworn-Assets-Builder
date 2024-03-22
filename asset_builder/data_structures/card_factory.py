"""
A file for matching the correct card type to its appropriate class
"""

from typing import Any, Dict
from asset_builder.data_structures.asset_card.asset import AssetCard

from asset_builder.data_structures.card import Card
from asset_builder.data_structures.card_types import CardType


def _get_card_type(card_data: Dict[str, Any]) -> CardType:
    """
    Returns the card type from the given card data
    """
    if "card_type" not in card_data:
        raise ValueError(
            f"Card data does not have mandatory field \"card_type\": {card_data}")

    available_card_types = [t.value for t in CardType]
    if card_data["card_type"] not in available_card_types:
        raise KeyError(f"Invalid card type: {repr(card_data['card_type'])}")

    return CardType(card_data["card_type"])


def get_card_by_type(card_data: Dict[str, Any]) -> Card:
    """
    Returns the card based on the card type
    """
    card_type = _get_card_type(card_data)
    if card_type == CardType.ASSET:
        return AssetCard.from_dict(card_data)

    raise KeyError(f"No renderers for card type {card_type}")
