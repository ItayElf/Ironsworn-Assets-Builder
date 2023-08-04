"""
The main file
"""
import pathlib
from renderer.context import Context
from renderer.head_renderer import render_head

OUTPUT_FILE = pathlib.Path(__file__).parent / \
    pathlib.Path("build", "output.html")


def save_output(content: str):
    """
    Saves the output to the output file
    """
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.touch(exist_ok=True)
    OUTPUT_FILE.write_text(content)


def main() -> None:
    """
    The main function
    """
    context = Context()

    with context.tag("html"):
        render_head(context)

    print(context.getvalue())
    save_output(context.getvalue())


if __name__ == "__main__":
    main()
