"""
A file for rendering images of assets
"""


import click
from html2image import Html2Image
from asset_builder.data_structures.asset import Asset
from asset_builder.data_structures.configuration import Configuration
from asset_builder.render.asset_renderer.asset_back_renderer import render_asset_back
from asset_builder.render.asset_renderer.renderer import render_asset
from asset_builder.render.context import Context
from asset_builder.render.head_renderer import render_head

PDF_SCALE = 0.4663937007874016
IMAGE_CSS = "body {background: white;margin: 0;}"
PDF_CSS = ".asset-background {scale: 0.4663937007874016}"
ASSET_SIZE = (375, 575)
PDF_ASSET_SIZE = (375 * PDF_SCALE, 575 * PDF_SCALE)


def get_asset_context(config: Configuration, asset: Asset) -> Context:
    """
    Returns the context of an asset card
    """
    context = Context(**config.settings)

    with context.tag("html"):
        render_head(context)

        with context.tag("body"):
            render_asset(context, asset)

    return context


def get_back_context(config: Configuration, asset_type: str) -> Context:
    """
    Returns the context of an asset back
    """
    context = Context(**config.settings)

    with context.tag("html"):
        render_head(context)

        with context.tag("body"):
            render_asset_back(context, asset_type)

    return context


def render_assets_images(config: Configuration, hti: Html2Image, for_pdf: bool = False):
    """
    Renders images for assets
    """
    css = IMAGE_CSS
    if for_pdf:
        css += PDF_CSS

    with click.progressbar(config.assets, label="Rendering assets") as progress_bar:
        for asset in progress_bar:
            context = get_asset_context(config, asset)
            hti.screenshot(
                html_str=context.getvalue(),
                css_str=IMAGE_CSS,
                save_as=f"{asset.name}.png",
                size=PDF_ASSET_SIZE if for_pdf else ASSET_SIZE
            )


def render_assets_backs(config: Configuration, hti: Html2Image, for_pdf: bool = False):
    """
    Renders backs for assets
    """
    css = IMAGE_CSS
    if for_pdf:
        css += PDF_CSS

    asset_types = set(asset.type for asset in config.assets)
    with click.progressbar(asset_types, label="Rendering asset backs") as progress_bar:
        for asset_type in progress_bar:
            context = get_back_context(config, asset_type)
            hti.screenshot(
                html_str=context.getvalue(),
                css_str=IMAGE_CSS,
                save_as=f"{asset_type}.png",
                size=PDF_ASSET_SIZE if for_pdf else ASSET_SIZE
            )


def render_images(config: Configuration, output_dir: str, for_pdf: bool = False):
    """
    Saves assets as images
    """
    hti = Html2Image(output_path=output_dir)

    render_assets_images(config, hti, for_pdf)
    render_assets_backs(config, hti, for_pdf)
