#!/usr/bin/env python3

import jdp
import random

client = jdp.Client(("localhost", 11000))
client.send([{ "a" : 3.1415926535897932, "b" : [ "c" ] }, -1])
