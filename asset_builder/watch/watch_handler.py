"""
A file for storing the watch handler
"""

import pathlib
from typing import Callable
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class WatchHandler(FileSystemEventHandler):
    """
    A custom handler for detecting changes to the config file
    """

    def __init__(self, config_file: str, on_modified: Callable[[str], None]):
        self._config_file = pathlib.Path(config_file).absolute()
        self._on_modified = on_modified

    def on_modified(self, event):
        if pathlib.Path(event.src_path).absolute() == self._config_file:
            self._on_modified(str(self._config_file))

    def start_watch(self):
        """
        Starts observing on changes
        """
        observer = Observer()
        config_parent = pathlib.Path(self._config_file).parent
        observer.schedule(self, str(config_parent))
        observer.start()
        try:
            while observer.is_alive():
                observer.join(1)
        finally:
            observer.stop()
            observer.join()
