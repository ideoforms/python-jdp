#!/usr/local/bin/python

import jdp
import random

client = jdp.Client(("localhost", 11000))
client.send({ "hello" : "world" })

obj = {}
for n in range(500):
	obj[n] = random.randint(0, 500)
# client.send(obj)
client.send([ { "a" : 3.1415926535897932, "b" : [ "c" ] }, -1 ])
