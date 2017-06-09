#!/usr/bin/python 

class AbstractSecurityClient(): 
	def __init__(self, id, passwd):
		self.id = id 
		self.passwd = passwd
		self.init(id, passwd)
	
	def init(self, id, passwd): 
		pass 
		
	def login(self): 
		pass 
		
	def logout(self): 
		pass
		
	