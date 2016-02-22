import threading
import socket
import json

class Server:
	def __init__(self, port = 11000, hostname = "0.0.0.0"):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind((hostname, port))
		self.thread = None
		self.callbacks = []

	def start(self):
		self.thread = threading.Thread(target = self.server_thread)
		self.thread.setDaemon(True)
		self.thread.start()
	
	def add_callback(self, callback):
		self.callbacks.append(callback)

	def server_thread(self):
		while True:
			buf = self.sock.recv(65535)
			data = json.loads(buf)
			for callback in self.callbacks:
				callback(data)

class Client:
	def __init__(self, address):
		self.hostname, self.port = address
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	def send(self, data):
		data_string = json.dumps(data)
		self.sock.sendto(data_string, (self.hostname, self.port))
