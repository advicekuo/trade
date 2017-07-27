#!/usr/bin/python 
import AbstractSecurityClient
import win32com.client
import ctypes 
class IFbs_MsgServ2Events:
	def OnStatus(self, bsMsgID, bsMsgKey, nStatus):
		print "OnStatus : bsMsgID=[" + str(bsMsgID) + "] bsMsgKey=[" + str(bsMsgKey) + "] nStatus=[" + str(nStatus) + "]"
		
	def OnInstantData(self, bsMsgID, bsMsgKey, bsData):
		print "OnInstantData : bsMsgID=[" + str(bsMsgID) + "] bsMsgKey=[" + str(bsMsgKey) + "] nStatus=[" + str(nStatus) + "]"
		
class FubonSecurityClient(AbstractSecurityClient.AbstractSecurityClient): 
	def init(self, id, passwd):
		self.my_api = win32com.client.Dispatch("FubonE01API.Fubon_Mananger_API_2") 
		self.my_axMsgServer1 = win32com.client.DispatchWithEvents("FubonE01API.Fbs_MsgServ2", IFbs_MsgServ2Events) 
		# print self.my_api
		# print self.my_axMsgServer1
		# self.my_axMsgServer1.MsgServer_Connect(self.my_api)
		# self.my_axMsgServer1.MsgServer_Disconnect()
		
		
	def login(self): 
		if (self.my_axMsgServer1 != ''): 
			print "Log in with message service" 
			ret = self.my_api.eLogin_MsgServ(self.id, self.passwd, self.my_axMsgServer1, '')
		else: 
			print "Log in without message service" 
			ret = self.my_api.eLogin(self.id, self.passwd, '')
		
		errorCode = ret[0]
		if (errorCode >= 0): 
			print "Connect to server successfully. return:", errorCode 
		else: 
			print "Cannot connect to server, error code:", errorCode
		
	def logout(self): 
		print "Log out" 
		self.my_api.eLogout()

def main():
	f = open("D:\\pwa\\trade\\account.txt", "r").readlines()
	f = [x.strip() for x in f]
	print f 
	
	try: 
		a = FubonSecurityClient(f[0], f[1])
		a.login()
		a.logout()	
	except: 
		print "Cannot found account info."
		
if __name__ == '__main__':
    main()
	
	