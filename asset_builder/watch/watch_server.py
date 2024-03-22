"""
A file for creating the server for refetching

Most of this code is copy pasted from http.server
"""
import contextlib
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import pathlib
import socket
import sys
import tempfile
import threading
from typing import Any

SERVER_DIRECTORY = pathlib.Path(tempfile.gettempdir(), "assetBuilder")


class LoglessServer(SimpleHTTPRequestHandler):
    def log_message(self, *args: Any) -> None:
        return


class DualStackServer(ThreadingHTTPServer):

    def server_bind(self):
        # suppress exception when protocol is IPv4
        with contextlib.suppress(Exception):
            self.socket.setsockopt(
                socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
        return super().server_bind()

    def finish_request(self, request, client_address):
        self.RequestHandlerClass(request, client_address, self,
                                 directory=SERVER_DIRECTORY)  # type: ignore


def _get_best_family(*address):
    infos = socket.getaddrinfo(
        *address,
        type=socket.SOCK_STREAM,
        flags=socket.AI_PASSIVE,
    )
    family, _, __, ___, sockaddr = next(iter(infos))
    return family, sockaddr


def run(HandlerClass=LoglessServer,
        ServerClass=DualStackServer,
        protocol="HTTP/1.0", port=8000, bind=None):
    """Test the HTTP request handler class.

    This runs an HTTP server on port 8000 (or the port argument).

    """
    ServerClass.address_family, addr = _get_best_family(bind, port)
    HandlerClass.protocol_version = protocol
    with ServerClass(addr, HandlerClass) as httpd:  # type: ignore
        host, port = httpd.socket.getsockname()[:2]
        url_host = f'[{host}]' if ':' in host else host
        print(
            f"Serving HTTP on {host} port {port} "
            f"(http://{url_host}:{port}/) ..."
        )
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received, exiting.")
            sys.exit(0)


def start_server_thread():
    """
    Starts the server
    """
    threading.Thread(target=run, daemon=True).start()
