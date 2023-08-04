"""
The main file
"""
from renderer.context import Context


def main() -> None:
    """
    The main function
    """
    context = Context()

    print(context.getvalue())


if __name__ == "__main__":
    main()
