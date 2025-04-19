#!/usr/bin/env python3

#--------------------------------------------------------------------------------
# Simple example client for the jdp package.
# Sends a JSON-encoded object to a JDP server.
#--------------------------------------------------------------------------------

from jdp import JDPClient


def main():
    client = JDPClient("127.0.0.1", 48000)
    data = {
        "a": 3.1415926535897932,
        "b": ["c"]
    }
    client.send(data)
    print(f"Sent data to {client.host}:{client.port}")


if __name__ == "__main__":
    main()
