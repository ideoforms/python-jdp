#!/usr/bin/env python3

#--------------------------------------------------------------------------------
# Simple example server for the jdp package.
# Listens for JSON-encoded objects from a client and prints them to the console.
#--------------------------------------------------------------------------------

from jdp import JDPServer
import pprint

def main():
    def handler(data):
        pprint.pprint(data)

    server = JDPServer()
    server.add_callback(handler)
    server.start()
    print(f"Started JDP server on {server.ip}:{server.port}")
    print(f"Press Ctrl+C to stop the server.")

    try:
        server.wait()
    except KeyboardInterrupt:
        print("\nStopping server...")
        server.stop()
        
if __name__ == "__main__":
    main()
