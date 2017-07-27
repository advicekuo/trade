#!/usr/bin/python 

class AbstractAnalyzer(): 
	def __init__(self, stockId):
		self.stockId = stockId 
		self.init(stockId)
	
	def init(self, stockId): 
		pass 
		
	def analyze(self): 
		pass 
	