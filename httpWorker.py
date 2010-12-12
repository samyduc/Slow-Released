
# TAD courtesy #

# deckardfr aka Samy Duc #
# mail : samy.duc@gmail.com !

# fork me !

import random
import urlparse

class httpWorker:

	# const
	# array are used to build random packets
	# HTTP
	HTTP_POST = "POST"
	HTTP_VERSION = ["HTTP/1.0", "HTTP/1.1"]
	# serious stuff, courtesy for my mac*** girlfriend
	USER_AGENT = ["User-Agent: Opera/9.80 (Windows NT 6.1; U; en) Presto/2.6.30 Version/10.63",\
		"Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.2.12) Gecko/20101026 Firefox/3.6.12",\
		"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; fr-ca)",\
		"AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
		"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.12 (KHTML, like Gecko) Chrome/9.0.581.0 Safari/534.12",\
		"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.18) Gecko/2010042101 Iceweasel/3.0.6 (Debian-3.0.6-3)",\
		"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",\
	]
	HTTP_ACCEPT = ["text/html, application/xhtml+xml, */*",\
		"text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1",\
	]
	HTTP_ACCEPT_LANGUAGE = ["Accept-Language: fr-FR,fr;q=0.9,en;q=0.8",\
		"fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4",\
		"en-CA;q=0.8,en;q=0.6",\
	]
	HTTP_ACCEPT_CHARSET = ["ISO-8859-1,utf-8;q=0.7,*;q=0.3",\
		"ISO-8859-1,utf-8;q=0.7,*;q=0.7",\
	]
	HTTP_ACCEPT_ENCODING = ["gzip,deflate,sdch",\
		"gzip, deflate",\
		"deflate, gzip, x-gzip, identity, *;q=0",\
	]
	HTTP_CONNECTION  = ["Keep-Alive"]
	HTTP_CONTENT_TYPE = ["application/x-www-form-urlencoded",\
	]
	
	# SETTINGS
	# magic number
	MIN_LENGTH = 150
	MAX_LENGTH = 2458
	
	PAYLOAD_CHARSET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.=?!"
	
	# init http worker without knowing of timeout timer
	# on server side
	def __init__(self, url="http://localhost/?lol=true&urlparse=1"):
		self.url = urlparse.urlparse(url)
		print(self.url)
		# generate length of the packet
		# note : do not generate data
		self.data_length_max = random.randint(self.MIN_LENGTH, self.MAX_LENGTH)
		self.data_length_index = random.randint(1, self.MIN_LENGTH)
		
		# must be called at the end
		self.forgePOST();
	
	def forgePayload(self, length):
		payload = ""
		for i in range(0, length):
			payload += self.PAYLOAD_CHARSET[random.randint(0, len(self.PAYLOAD_CHARSET)-1)]
		return payload
	
	# forge http packet with random settings
	# not very elegant
	def forgePOST(self):
	
		if(self.url.query != ""):
			url_trailer = "?"
		else:
			url_trailer = ""
		
		# build http header
		self.http_header = self.HTTP_POST + " "
		self.http_header += self.url.path + url_trailer + self.url.query + " "
		self.http_header += random.choice(self.HTTP_VERSION) + "\r\n"
		self.http_header += "User-Agent: " + random.choice(self.USER_AGENT) + "\r\n"
		self.http_header += "Host: " + self.url.netloc + "\r\n"
		self.http_header += "Accept: " + random.choice(self.HTTP_ACCEPT) + "\r\n"
		self.http_header += "Accept-Language: " + random.choice(self.HTTP_ACCEPT_LANGUAGE) + "\r\n"
		self.http_header += "Accept-Charset: " + random.choice(self.HTTP_ACCEPT_CHARSET) + "\r\n"
		self.http_header += "Accept-Encoding: " + random.choice(self.HTTP_ACCEPT_ENCODING) + "\r\n"
		self.http_header += "Connection: " + random.choice(self.HTTP_CONNECTION) + "\r\n"
		
		# WARNING : THIS IS THE ONLY INTERESTING PART OF THE CODE
		self.http_header += "Content-Length: " + str(self.data_length_max) + "\r\n"
		
		# boring again
		self.http_header += "Content-Type: " + random.choice(self.HTTP_CONTENT_TYPE) + "\r\n"
		
		self.http_header += "\r\n"
		
		print(self.http_header)
		
		# build body
		self.http_msg = self.http_header
		self.http_msg += self.forgePayload(self.data_length_index)
		
	def nextMSG(self):
		toReturn = self.http_msg
		
		self.http_msg = self.http_header
		
		# length of data remaining
		# if no data remaining
		if((self.data_length_max-self.data_length_index) == 0):
			return ""
		else:
			length = random.randint(1, self.data_length_max-self.data_length_index)
			self.http_msg += self.forgePayload(length)
			self.data_length_index += length
			return self.http_msg
		