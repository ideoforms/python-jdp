#!/usr/bin/env python

from setuptools import setup

setup(
	name = 'jdp',
	version = '0.1.0',
	description = 'JSON Datagram Protocol',
	long_description = 'JSON Datagram Protocol, a lightweight communication protocol encapsulating JSON objects in individual UDP datagrams.',
	author = 'Daniel Jones',
	author_email = 'dan-code@erase.net',
	url = 'https://github.com/ideoforms/python-jdp',
	packages = ['jdp'],
	keywords = ('networking', 'json', 'communications', 'udp'),
	classifiers = [
		'Topic :: System :: Networking',
		'Topic :: Communications',
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers'
	]
)
