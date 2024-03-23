"""
A file to render printable pdf of assets
"""
import pathlib
from typing import List
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from asset_builder.data_structures.asset_card.asset import AssetCard
from asset_builder.data_structures.card import Card

from asset_builder.data_structures.configuration import Configuration

CARDS_IN_PAGE = 9
CARD_SIZE = (61.7 * mm, 94.5 * mm)

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


def render_card_page(canvas: Canvas, cards: List[Card], images_dir: str):
    """
    Renders a page of asset cards
    """
    for i, card in enumerate(cards):
        canvas.drawImage(
            pathlib.Path(images_dir, f"{card.name}.png"),
            *POSITIONS[i], *CARD_SIZE,
            preserveAspectRatio=True
        )
    canvas.showPage()


def render_card_backs(canvas: Canvas, cards: List[Card], images_dir: str):
    """
    Renders card backs
    """
    for i, card in enumerate(cards):
        canvas.drawImage(
            pathlib.Path(images_dir, f"{card.card_back_hash}.png"),
            *POSITIONS[i], *CARD_SIZE,
            preserveAspectRatio=True
        )

    canvas.showPage()


def render_pdf(config: Configuration, images_dir: str, output_file: str):
    """
    Renders a printable assets pdf
    """
    canvas = Canvas(output_file, pagesize=A4)

    cards = sorted(config.cards, key=lambda x: (x.card_back_hash, x.name))
    chunks = [cards[i:i+CARDS_IN_PAGE]
              for i in range(0, len(cards), CARDS_IN_PAGE)]

    for chunk in chunks:
        render_card_page(canvas, chunk, images_dir)
        render_card_backs(canvas, chunk, images_dir)

    canvas.save()
