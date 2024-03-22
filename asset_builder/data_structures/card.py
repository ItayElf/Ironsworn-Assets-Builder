"""
A file for the generic card class
"""

import abc
from dataclasses import dataclass
from typing import Any, Dict

from asset_builder.data_structures.card_types import CardType
from asset_builder.render.context import Context


@dataclass
class Card:
    """
    An abstract class that represents a generic card that can be rendered
    """
    card_type: CardType

    def __post_init__(self):
        if self.card_type is str:
            self.card_type = CardType(self.card_type)

    @abc.abstractmethod
    def render(self, context: Context) -> str:
        """
        Renders the card and returns the HTML representation
        """

    @abc.abstractmethod
    def render_back(self, context: Context) -> str:
        """
        Renders the back of the card and returns the HTML representation
        """

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Card":
        """
        Returns a card object from a dict
        """
        return cls(**data)
