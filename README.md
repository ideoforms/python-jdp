# JSON Datagram Protocol

JSON Datagram Protocol, a lightweight communication protocol encapsulating JSON objects in individual UDP datagrams.

## Usage: Client

```python
import jdp

client = jdp.Client(("localhost", 11000))
client.send({ "hello" : "world" })
```

## Usage: Server

```python

def handler(data):
	print str(data)

server = jdp.Server(11000)
server.add_callback(handler)
server.start()
```

---

## License

> Created by Daniel Jones <http://www.erase.net>  
> Available under the terms of the MIT License.
