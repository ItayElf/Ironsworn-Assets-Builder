"""
A file for rendering abilities
"""
import markdown
from asset_builder.data_structures.asset_card.asset import AssetCard
from asset_builder.data_structures.asset_card.asset_ability import AssetAbility
from asset_builder.render.context import Context


def render_ability(context: Context, ability: AssetAbility):
    """
    Renders an ability
    """
    dot_classname = "dot filled" if ability.enabled else "dot unfilled"

    with context.tag("div", ("class", "asset-ability")):
        with context.tag("i", ("class", dot_classname)):
            pass

        with context.tag("div", ("class", "asset-ability-description")):
            if ability.name:
                with context.tag("span", ("class", "asset-ability-name")):
                    context.text(ability.name)

            with context.tag("span", ("class", "asset-ability-text")):
                context.asis(markdown.markdown(ability.text))


def render_asset_abilities(context: Context, asset: AssetCard):
    """
    Renders the abilities of the asset
    """
    with context.tag("div", ("class", "asset-abilities")):
        for ability in asset.abilities:
            render_ability(context, ability)
