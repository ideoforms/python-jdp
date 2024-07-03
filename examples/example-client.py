#!/usr/bin/env python3

import jdp


def main():
    client = jdp.Client(("localhost", 48000))
    client.send({
        "a": 3.1415926535897932,
        "b": ["c"]
    })


if __name__ == "__main__":
    main()
