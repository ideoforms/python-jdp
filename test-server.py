#!/usr/local/bin/python

import jdp
import time
import pprint

def read(data):
	# print data["hello"]
	pprint.pprint(data)

server = jdp.Server(11000)
server.add_callback(read)
server.start()

while True:
	time.sleep(0.1)
