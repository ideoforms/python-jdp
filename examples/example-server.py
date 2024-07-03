#!/usr/bin/env python3

import jdp
import time
import pprint

def main():
    def handler(data):
        pprint.pprint(data)

    server = jdp.Server(48000)
    server.add_callback(handler)
    server.start()

    while True:
        time.sleep(0.1)
        
if __name__ == "__main__":
    main()