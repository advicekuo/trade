#!/usr/bin/python 
import AbstractSecurityClient
import ctypes
import win32com.client

class FubonSecurityClient(AbstractSecurityClient.AbstractSecurityClient): 
	def init(self, id, passwd):
		# fubonOcx = ctypes.WinDLL("c:\\Windows\\System32\\FubonE01API.ocx") 
		# clsid_Fubon_Mananger_API_2 = "{98F7A444-661E-42D3-AAFE-CFE106E020DA}" 
		clsid_Fubon_Mananger_API_2 = "{E7001FA2-1C1E-4AE3-AED3-B2DC6EB03443}" #coclass
		# clsid_Fubon_Mananger_API_2 = "{6271895B-E67F-4DEE-B68B-BF74ACE07753}" 
		class_Fubon_Mananger_API_2 = win32com.client.gencache.GetClassForProgID(clsid_Fubon_Mananger_API_2)
		print class_Fubon_Mananger_API_2
		# a = class_Fubon_Mananger_API_2()
	
	def login(self): 
		pass 
		
	def logout(self): 
		pass

def main():
    a = FubonSecurityClient(0,0) 

if __name__ == '__main__':
    main()