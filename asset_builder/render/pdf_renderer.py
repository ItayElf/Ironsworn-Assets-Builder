"""
A file to render printable pdf of assets
"""
import pathlib
from typing import List
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from asset_builder.data_structures.asset import Asset

from asset_builder.data_structures.configuration import Configuration

ASSETS_IN_PAGE = 9
ASSET_SIZE = (61.7 * mm, 94.5 * mm)

POSITIONS = [
    (12.4*mm, 196.8*mm),
    (74.1*mm, 196.8*mm),
    (135.8*mm, 196.8*mm),
    (12.4*mm, 102.3*mm),
    (74.1*mm, 102.3*mm),
    (135.8*mm, 102.3*mm),
    (12.4*mm, 7.8*mm),
    (74.1*mm, 7.8*mm),
    (135.8*mm, 7.8*mm),
]


def render_asset_page(canvas: Canvas, assets: List[Asset], images_dir: str):
    """
    Renders a page of asset cards
    """
    for i, asset in enumerate(assets):
        canvas.drawImage(
            pathlib.Path(images_dir, f"{asset.name}.png"),
            *POSITIONS[i], *ASSET_SIZE,
            preserveAspectRatio=True
        )
    canvas.showPage()


def render_asset_backs(canvas: Canvas, assets: List[Asset], images_dir: str):
    """
    Renders card backs
    """
    for i, asset in enumerate(assets):
        canvas.drawImage(
            pathlib.Path(images_dir, f"{asset.type}.png"),
            *POSITIONS[i], *ASSET_SIZE,
            preserveAspectRatio=True
        )

    canvas.showPage()


def render_pdf(config: Configuration, images_dir: str, output_file: str):
    """
    Renders a printable assets pdf
    """
    canvas = Canvas(output_file, pagesize=A4)

    assets = sorted(config.assets, key=lambda x: (x.type, x.name))
    chunks = [assets[i:i+ASSETS_IN_PAGE]
              for i in range(0, len(assets), ASSETS_IN_PAGE)]

    for chunk in chunks:
        render_asset_page(canvas, chunk, images_dir)
        render_asset_backs(canvas, chunk, images_dir)

    canvas.save()
