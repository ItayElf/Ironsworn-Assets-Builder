"""
The main file
"""
import pathlib
from data_structures.asset import Asset
from data_structures.asset_ability import AssetAbility
from render.context import Context
from render.head_renderer import render_head
from render.asset_renderer.renderer import render_asset

OUTPUT_FILE = pathlib.Path("build", "output.html")

ASSET = Asset(
    "Ironclad",
    "PATH",
    [
        AssetAbility("this is the text", "Titled", True),
        AssetAbility("Short"),
        AssetAbility("Long " + "AAAA " * 30)
    ],
    write_ins=["First", "Second"],
    description="Test description",
    track=4
)


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
    context = Context(rtl=True)

    with context.tag("html"):
        render_head(context)

        with context.tag("body"):
            render_asset(context, ASSET)

    print(context.getvalue())
    save_output(context.getvalue())


if __name__ == "__main__":
    main()
