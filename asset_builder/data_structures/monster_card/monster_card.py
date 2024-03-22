"""
A file for the monster card
"""

from dataclasses import dataclass, field
from typing import List, Optional, override

from asset_builder.data_structures.card import Card
from asset_builder.render.context import Context


@dataclass
class MonsterCard(Card):
    """
    A card representing a monster
    """
    name: str
    rank: str
    type: str
    features: List[str]
    drives: List[str]
    tactics: List[str]
    terrain: Optional[List[str]] = field(default=None)
    description: Optional[str] = field(default=None)
    icon_path: Optional[str] = field(default=None)

    @override
    def render(self, context: Context) -> str:
        return ""

    @override
    def render_back(self, context: Context) -> str:
        return ""

    @override
    @property
    def card_back_hash(self):
        return self.rank
