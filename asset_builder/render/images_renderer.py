"""
A file for rendering images of assets
"""


import click
from html2image import Html2Image
from asset_builder.data_structures.card import Card
from asset_builder.data_structures.configuration import Configuration
from asset_builder.render.context import Context
from asset_builder.render.head_renderer import render_head

IMAGE_CSS = "body {background: white;margin: 0;}"
CARD_SIZE = (375, 575)


def get_card_context(config: Configuration, card: Card) -> Context:
    """
    Returns the context of an asset card
    """
    context = Context(**config.settings)

    with context.tag("html"):
        render_head(context)

        with context.tag("body"):
            card.render(context)

    return context


def get_back_context(config: Configuration, card: Card) -> Context:
    """
    Returns the context of an asset back
    """
    context = Context(**config.settings)

    with context.tag("html"):
        render_head(context)

        with context.tag("body"):
            card.render_back(context)

    return context


def render_assets_images(config: Configuration, hti: Html2Image):
    """
    Renders images for assets
    """
    with click.progressbar(config.cards, label="Rendering cards") as progress_bar:
        for card in progress_bar:
            context = get_card_context(config, card)
            hti.screenshot(
                html_str=context.getvalue(),
                css_str=IMAGE_CSS,
                save_as=f"{card.name}.png",
                size=CARD_SIZE
            )


def render_assets_backs(config: Configuration, hti: Html2Image):
    """
    Renders backs for assets
    """
    unique_backs = {card.card_back_hash: card for card in config.cards}
    with click.progressbar(unique_backs.values(), label="Rendering card backs") as progress_bar:
        for card in progress_bar:
            context = get_back_context(config, card)
            hti.screenshot(
                html_str=context.getvalue(),
                css_str=IMAGE_CSS,
                save_as=f"{card.card_back_hash}.png",
                size=CARD_SIZE
            )


def render_images(config: Configuration, output_dir: str):
    """
    Saves assets as images
    """
    hti = Html2Image(output_path=output_dir, disable_logging=True)

    render_assets_images(config, hti)
    render_assets_backs(config, hti)
