"""
A file that holds the configuration dataclass 
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List

from asset_builder.data_structures.card import Card
from asset_builder.data_structures.card_factory import get_card_by_type


@dataclass
class Configuration:
    """
    A class that represents the configuration of the program
    """
    cards: List[Card]
    settings: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> "Configuration":
        """
        Takes a json object and returns a configuration from it
        """
        if not "cards" in data:
            raise KeyError(
                f"Configuration data doesn't have mandatory field 'cards': {
                    data}"
            )

        data["cards"] = [get_card_by_type(card) for card in data["cards"]]
        return cls(**data)
