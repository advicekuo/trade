#!/usr/bin/python 
import AbstractSecurityClient
import ctypes
import win32com.client

class FubonSecurityClient(AbstractSecurityClient.AbstractSecurityClient): 
	def init(id, passwd):
		fubonOcx = ctypes.WinDLL("c:\\Windows\\System32\\FubonE01API.ocx") 
		
	
	def login(self): 
		pass 
		
	def logout(self): 
		pass
