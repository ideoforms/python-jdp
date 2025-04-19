import socket
import json
from typing import Union

class JDPClient:
    def __init__(self, host: str, port: int):
        """
        Create an instance of a JSON Datagram Protocol (JDP) client.

        Args:
            host (str): The hostname or IP address of the server to send data to.
            port (int): The port number of the server to send data to.
        """
        self.host, self.port = host, port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, data: Union[int, float, str, list, dict]):
        """
        Send a JSON-encoded object to the server.
        Typically, this will be a dictionary, but other JSON-encodable types are supported.

        Args:
            data (Union[int, float, str, list, dict]): The JSON-encodable object to send.
        """
        data_string = json.dumps(data)
        data_string = data_string.encode()
        self.sock.sendto(data_string, (self.host, self.port))
