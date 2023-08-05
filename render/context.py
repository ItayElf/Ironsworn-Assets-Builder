"""
A file that contains the context class
"""
from yattag.doc import Doc


class Context:
    """
    A class that represents the render context
    """

    def __init__(self, rtl=False) -> None:
        self._rtl = rtl
        self._doc, self._tag, self._text = Doc().tagtext()

    def _set_rtl(self, *args) -> list:
        """
        Returns new rtl class for the tag
        """
        new_args = []
        for arg in args:
            if isinstance(arg, tuple) and arg[0] == "class":
                new_args.append(("class", arg[1] + " rtl"))
            else:
                new_args.append(arg)
        return new_args

    def tag(self, tag_name: str, *args, **kwargs):
        """
        Creates an html tag
        """
        if self._rtl:
            args = self._set_rtl(*args)

        return self._tag(tag_name, *args, **kwargs)

    def text(self, *strings: str):
        """
        Adds text to the current tag
        """
        return self._text(*strings)

    def asis(self, *strings: str):
        """
        Adds unescaped html
        """
        return self._doc.asis(*strings)

    def getvalue(self) -> str:
        """
        Returns the whole document as a single string
        """
        return self._doc.getvalue()
