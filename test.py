# TAD courtesy #

# deckardfr aka Samy Duc #
# mail : samy.duc@gmail.com !

# fork me !

from probe import *

import re

class Test:

	def __init__(self):
		help = "help : python probe.py [-u=XXX : url] URL [-p=80 : port] [-s probe] [-a=time : attack with given time] [-ap : get time and attack] [? : help]"
	
		self.probe = False
		self.attack = False
		self.timer = 0
		
		self.url = ""
		self.port = 80
		
		self.safe = True
		
		# ugly interface
		for arg in sys.argv:
			
			if(arg == sys.argv[0]):
				pass
			elif(arg[:3] == "-p=" and len(arg) >= 4):
				# port
				self.port = (int)(arg[3:])
			elif(arg == "-s"):
				# probing
				self.probe = True
			elif(arg == "-ap"):
				self.probe = True
				self.attack = True
			elif(arg[:3] == "-a=" and len(arg) >= 4):
				self.timer = (int)(arg[3:])
			elif(arg[:3] == "-u=" and len(arg) >= 4):
				self.url = arg[3:]
				if(self.url[:len("http")] != "http"):
					self.url = "http://" + self.url
				# if no args and less than 3 /, we add a trailer /
				if(self.url.count("3") < 3):
					self.url += "/"
			else:
				print(help)
				self.safe = False
				break

	def probing(self):
	
		test = Probe(self.url, self.port, 0)
		test.probe()
	
		return test.slow
	
	def attacking(self):
		pass
					
	def main(self):
		if(self.safe):
			if(self.probe):
				self.timer = self.probing()
			if(self.attack):
				self.attacking()
	
	
if __name__ == "__main__" :
	test = Test()
	test.main()