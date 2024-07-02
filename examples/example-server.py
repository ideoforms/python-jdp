#!/usr/bin/env python3

import jdp
import time
import pprint

def read(data):
    pprint.pprint(data)

server = jdp.Server(11000)
server.add_callback(read)
server.start()

while True:
    time.sleep(0.1)
