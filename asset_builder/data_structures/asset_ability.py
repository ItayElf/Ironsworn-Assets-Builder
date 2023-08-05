"""
A file that holds the asset ability dataclass 
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AssetAbility:
    """
    A class that represents an asset's ability
    """
    text: str
    name: Optional[str] = field(default=None)
    enabled: bool = field(default=False)
