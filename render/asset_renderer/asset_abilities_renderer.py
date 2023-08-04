"""
A file for rendering abilities
"""
from data_structures.asset import Asset
from data_structures.asset_ability import AssetAbility
from render.context import Context


def render_ability(context: Context, ability: AssetAbility):
    """
    Renders an ability
    """
    dot_classname = "dot filled" if ability.enabled else "dot unfilled"

    with context.tag("div", ("class", "asset-ability")):
        with context.tag("i", ("class", dot_classname)):
            pass

        if ability.name:
            with context.tag("span", ("class", "asset-ability-name")):
                context.text(ability.name)

        with context.tag("span", ("class", "asset-ability-text")):
            context.text(ability.text)


def render_asset_abilities(context: Context, asset: Asset):
    """
    Renders the abilities of the asset
    """
    with context.tag("div", ("class", "asset-abilities")):
        for ability in asset.abilities:
            render_ability(context, ability)