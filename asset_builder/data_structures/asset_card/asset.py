"""
A file that holds the asset dataclass 
"""

from dataclasses import dataclass, field
from typing import Any, Dict, Optional, List, Union, override

from asset_builder.data_structures.asset_card.asset_ability import AssetAbility
from asset_builder.data_structures.card import Card
from asset_builder.render.card_back_renderer import render_card_back
from asset_builder.render.context import Context


@dataclass
class AssetCard(Card):
    """
    A class that represents an asset
    """
    name: str
    type: str
    abilities: List[AssetAbility]
    write_ins: Optional[List[str]] = field(default=None)
    description: Optional[str] = field(default=None)
    icon_path: Optional[str] = field(default=None)
    track: Optional[Union[int, List[str]]] = field(default=None)

    @override
    def render(self, context: Context) -> str:
        # Ugly hack to solve circular import
        from asset_builder.render.asset_renderer.renderer import render_asset  # pylint: disable=import-outside-toplevel

        return render_asset(context, self)

    @override
    def render_back(self, context: Context) -> str:
        return render_card_back(context, self.type)

    @override
    @property
    def card_back_hash(self):
        return self.type

    @override
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AssetCard":
        """
        Takes a json object and returns an asset from it
        """
        if not "abilities" in data:
            raise KeyError(
                f"Asset data doesn't have mandatory field 'attributes': {data}"
            )

        data["abilities"] = [AssetAbility(**ability)
                             for ability in data["abilities"]]

        return cls(**data)
