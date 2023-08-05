"""
A file that holds the configuration dataclass 
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List

from data_structures.asset import Asset


@dataclass
class Configuration:
    """
    A class that represents the configuration of the program
    """
    assets: List[Asset]
    settings: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> "Configuration":
        """
        Takes a json object and returns a configuration from it
        """
        if not "assets" in data:
            raise KeyError(
                f"Configuration data doesn't have mandatory field 'assets': {data}"
            )

        data["assets"] = [Asset.from_json(asset) for asset in data["assets"]]
        return cls(**data)
