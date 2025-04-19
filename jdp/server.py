import threading
import socket
import json
from typing import Callable


class JDPServer:
    def __init__(self,
                 port: int = 48000,
                 ip: str = "0.0.0.0"):
        """
        Create an instance of a JSON Datagram Protocol (JDP) server.
        This server listens for incoming JSON-encoded UDP packets on the specified
        port and IP address.

        The server must be started using the `start` method.

        Args:
            port (int, optional): The port to listen on. Defaults to 48000.
            ip (str, optional): The IP address to listen on. Defaults to "0.0.0.0",
                                which means all available interfaces.
        """
        self.port = port
        self.ip = ip
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(0.1)
        self.thread = None
        self.callbacks = []
        self.is_running = False

    def start(self):
        """
        Start the server to listen for incoming UDP packets.
        """
        if self.is_running:
            return
        
        self.is_running = True
        self.sock.bind((self.ip, self.port))
        self.thread = threading.Thread(target=self._server_thread, daemon=True)
        self.thread.start()

    def stop(self):
        """
        Stop the server and close the socket.
        """
        if not self.is_running:
            return
        
        self.is_running = False
        if self.thread is not None:
            self.thread.join()
        self.sock.close()

    def add_callback(self, callback: Callable):
        """
        Add a callback function to be called when data is received.
        The callback function should accept a single argument, which will be the
        JSON-decoded data received from the client.

        Args:
            callback (Callable): The function to call when data is received.
        """
        self.callbacks.append(callback)
    
    def remove_callback(self, callback: Callable):
        """
        Remove a callback function from the list of callbacks.

        Args:
            callback (Callable): The callback function to remove.

        Raises:
            ValueError: If the callback is not found in the list of callbacks.
        """
        if callback in self.callbacks:
            self.callbacks.remove(callback)
        else:
            raise ValueError("Callback not found in the list of callbacks.")

    def wait(self):
        """
        Block the main thread until the server is stopped.
        """
        if self.thread is not None:
            self.thread.join()

    def _server_thread(self):
        """
        The main loop of the server that listens for incoming UDP packets.
        """
        while self.is_running:
            try:
                buf = self.sock.recv(65535)
                data = json.loads(buf)
                for callback in self.callbacks:
                    callback(data)
            except socket.timeout:
                pass