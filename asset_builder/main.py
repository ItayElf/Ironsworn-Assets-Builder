"""
The main file
"""
import json
import pathlib

import click
from asset_builder.data_structures.asset import Asset
from asset_builder.data_structures.asset_ability import AssetAbility
from asset_builder.data_structures.configuration import Configuration
from asset_builder.render.body_renderer import render_asset_group
from asset_builder.render.context import Context
from asset_builder.render.head_renderer import render_head

OUTPUT_FILE = pathlib.Path("build", "output.html")

ASSET = Asset(
    "לוחם חרב",
    "נתיב",
    [
        AssetAbility("זה *הטקסט* פה יש **מילים**", "כותרת", True),
        AssetAbility("קצר"),
        AssetAbility("*ארוך* " + "ארוך " * 30)
    ],
    write_ins=["ראשון", "שני"],
    description="תיאור בדיקה",
    track=4
)


def load_configuration(filename: str) -> Configuration:
    """
    Returns a configuration object from a file
    """
    data = json.loads(pathlib.Path(filename).read_text(encoding="utf-8"))
    return Configuration.from_json(data)


def save_output(content: str):
    """
    Saves the output to the output file
    """
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.touch(exist_ok=True)
    OUTPUT_FILE.write_text(content, encoding="utf-8")


def main() -> None:
    """
    The main function
    """
    configuration = load_configuration("example.json")
    context = Context(**configuration.settings)

    with context.tag("html"):
        render_head(context)

        with context.tag("body"):
            render_asset_group(context, configuration.assets)

    print(context.getvalue())
    save_output(context.getvalue())


@click.command()
def cli():
    """
    The cli function
    """
    click.echo("Hello World")


if __name__ == "__main__":
    main()
