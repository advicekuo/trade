#!/usr/bin/python 
import AbstractSecurityClient
import win32com.client
import ctypes 

class FubonSecurityClient(AbstractSecurityClient.AbstractSecurityClient): 
	def init(self, id, passwd):
		
		clsid_Fubon_Mananger_API_2       = "{60F749A4-6180-42BA-B9A3-5F2F657809DC}" #  
		# clsid_Fbs_MsgServ2               = "{1A2CEB38-FAB7-434C-B797-D2978FD6908D}" #  
		# clsid_Fbs_MsgServ2               = "{ABB84942-39DD-40CB-A176-8C508EE59CAD}" # 
		clsid_Fbs_MsgServ2               = "{A893A5A3-6619-4A7A-A7F4-50C02842F88F}" 
		
		# clsid_FutureTradeCOM_Test        = "{4B661E2A-9874-4534-B353-06F9C8E29B8C}" #  
		# clsid_Fubon_Mananger_MsgServer_2 = "{47C406EC-DDD0-48B3-B8B2-7529580C54DD}" #  
		
		
		self.my_api = win32com.client.Dispatch(clsid_Fubon_Mananger_API_2)
		# self.axMsgServer1 = '' 
		# for key in win32com.client.Dispatch(clsid_Fubon_Mananger_API_2).__dict__: 
			# print key 
		# print "---------------"
		# print self.my_api
		# self.axMsgServer1 = win32com.client.Dispatch(clsid_Fbs_MsgServ2)
		self.axMsgServer1 = win32com.client.gencache.GetClassForProgID(clsid_Fbs_MsgServ2)()
		print self.axMsgServer1._olecp
		# self.axMsgServer1._dispid_to_func_[1]
		
	def axMsgServer1_OnStatus(self, bsMsgID, bsMsgKey, nStatus):
		print "OnStatus : bsMsgID=[" + str(bsMsgID) + "] bsMsgKey=[" + str(bsMsgKey) + "] nStatus=[" + str(nStatus) + "]"
		
	def axMsgServer1_OnInstantData(self, bsMsgID, bsMsgKey, bsData):
		print "OnInstantData : bsMsgID=[" + str(bsMsgID) + "] bsMsgKey=[" + str(bsMsgKey) + "] nStatus=[" + str(nStatus) + "]"
		
	
	def login(self): 
		if (self.axMsgServer1 != ''): 
			self.my_api.eLogin_MsgServ(self.id, self.passwd, self.axMsgServer1, '')
		else: 
			# self.my_api.eLogin(ctypes.c_char_p(self.id), ctypes.c_char_p(self.passwd), '')
			self.my_api.eLogin(self.id, self.passwd, '')
		
	def logout(self): 
		self.my_api.eLogout()

def main():
	a = FubonSecurityClient('F127144892',0) 
	# a.login()
	# a.logout()

if __name__ == '__main__':
    main()