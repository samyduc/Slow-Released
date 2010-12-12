
# TAD courtesy #

# deckardfr aka Samy Duc #
# mail : samy.duc@gmail.com !

# fork me !

from httpWorker import *
import time
import urlparse
import socket
import sys


class Probe:
	def __init__(self, url="http://localhost/", port=80, slow=0):
		# i know
		self.http = httpWorker(url=url)
		self.slow = slow
		self.port = port
		self.sock = None
	
	def connect(self):
		if(self.sock == None):
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			# resolve name
			ip = socket.gethostbyname_ex(self.http.url.netloc)
			self.sock.connect((ip[2][0], self.port))
	
	def probe(self):
		# set time
		a_time = time.time()

		self.connect()
		
		data = "2"
		
		msg = self.http.http_msg
		
		self.sock.sendall(msg)
		
		# wait disconnection
		while(data != ""):
			data = self.sock.recv(1024)
			print(data)
		self.sock = None
		
		b_time = time.time()
		
		self.slow = b_time - a_time
		
		print("PROBING :" + str(self.slow))
		
	def push(self):
		self.Connect()
		
		while(True):
			try:
				msg = self.http.nextMSG()
				if(msg == ""):
					self.sock = None
					break
				else:
					self.sock.send(msg)
			except(socket.error):
				self.sock = None
				break
			sleep(self.slow - self.slow/100.0)
		





	
	
	