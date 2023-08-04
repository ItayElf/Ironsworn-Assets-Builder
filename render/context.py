"""
A file that contains the context class
"""
from yattag.doc import Doc


class Context:
    """
    A class that represents the render context
    """

    def __init__(self) -> None:
        self._doc, self._tag, self._text = Doc().tagtext()

    def tag(self, tag_name: str, *args, **kwargs):
        """
        Creates an html tag
        """
        return self._tag(tag_name, *args, **kwargs)

    def text(self, *strings: str):
        """
        Adds text to the current tag
        """
        return self._text(*strings)

    def getvalue(self) -> str:
        """
        Returns the whole document as a single string
        """
        return self._doc.getvalue()
