"""
A file that holds the asset dataclass 
"""

from dataclasses import dataclass, field
from typing import Any, Dict, Optional, List, Union

from data_structures.asset_ability import AssetAbility


@dataclass
class Asset:
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

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> "Asset":
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
