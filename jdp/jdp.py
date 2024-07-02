import threading
import socket
import json
from typing import Callable


class Server:
    def __init__(self,
                 port: int = 48000,
                 hostname: str = "0.0.0.0"):
        self.port = port
        self.hostname = hostname
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((hostname, port))
        self.thread = None
        self.callbacks = []

    def start(self):
        self.thread = threading.Thread(target=self.server_thread, daemon=True)
        self.thread.start()

    def add_callback(self, callback: Callable):
        self.callbacks.append(callback)

    def server_thread(self):
        while True:
            buf = self.sock.recv(65535)
            data = json.loads(buf)
            for callback in self.callbacks:
                callback(data)


class Client:
    def __init__(self, address: tuple[str, int]):
        self.hostname, self.port = address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, data: dict):
        data_string = json.dumps(data)
        data_string = data_string.encode()
        self.sock.sendto(data_string, (self.hostname, self.port))
