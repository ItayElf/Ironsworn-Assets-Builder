"""
The main file
"""
import pathlib
from data_structures.asset import Asset
from data_structures.asset_ability import AssetAbility
from render.body_renderer import render_asset_group
from render.context import Context
from render.head_renderer import render_head

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
            render_asset_group(context, [ASSET] * 9)

    print(context.getvalue())
    save_output(context.getvalue())


if __name__ == "__main__":
    main()
