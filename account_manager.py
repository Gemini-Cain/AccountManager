#@Date 2015/09/15
#@Author Xin Du
#coding:utf-8

import json
import dbhandler
import account

class AccountManager(object):
	"""账户管理类"""
	def __init__(self):
		super(AccountManager, self).__init__()
		self.handler = dbhandler.DBHandler("D:\\Code\\AccountManager\\test.txt")

	def add_account(self, account):
		accounts = self.handler.getAccounts()
		for item in accounts:
			if item.get_sign() == account.get_sign():
				#raise 
				return
		accounts.append(account)
		self.handler.saveAccounts(accounts)

	def delete_account(self, id):
		accounts = self.handler.getAccounts()
		for item in accounts:
			if item.get_id() == id:
				accounts.remove(item)
		self.handler.saveAccounts(accounts)

	def search_account(self, condition):
		for key in condition:
			if condition[key] is None or condition[key] == [] or condition[key] == "":
				del condition[key]
		result = []
		for item in self.handler.search(condition):
			result.append(account.Account(item["name"], item["sign"], item["website"], item["login_name"], 
				item["password"], item["tag"]))

		return result

	def change_account(self, account):
		accounts = self.handler.getAccounts()
		for item in accounts:
			if item.get_id() == account.get_id():
				print item.show_account()
				accounts.remove(item)
				accounts.append(account)
		self.handler.saveAccounts(accounts)

	def search(self, conditions):
		result = []
		accounts = self.handler.getAccounts()

		for item in accounts:
			is_exist = True
			for key in conditions.keys():
				if isinstance(item[key], unicode) and item[key] == conditions[key]:
					continue
				elif isinstance(item[key], list):
					for item in conditions[key]:
						if item in item[key]:
							continue
						else:
							
			else:
				raise KeyError
		if is_match == True:
			result.append(text)
		return result

def test():
	manager = AccountManager()
	ac = account.Account(name = str("豆瓣").decode("utf-8"), sign = "DB0", website = "www.douban.com", login_name = 
		{"username" : "dd", "mobile_phone" : "18665005621"}, password = {"login_password" : "123456", "pay_password" : "18665005621"}, tag = ["hot", "interesting"])
	manager.add_account(ac)

	#manager.delete_account("9364cde347921fec53854d78f3449fc3")

	ac = account.Account("9364cde347921fec53854d78f3449fc3", str("豆瓣").decode("utf-8"), "DB3", "www.douban.com", 
		{"username" : "xx", "mobile_phone" : "18665005621"}, {"login_password" : "123456", 
		"pay_password" : "18665005621"}, ["hot", "interesting"])
	manager.change_account(ac)

	# result = manager.search_account({"name":str("豆瓣").decode("utf-8")})
	# print str("----------根据名称查询----------").decode("utf-8")
	# for item in result:
	# 	item.show_account()

	# result = manager.search_account({"sign":"DB"})
	# print str("----------根据符号查询----------").decode("utf-8")
	# for item in result:
	# 	item.show_account()

	# result = manager.search_account({"website":"www.douban.com"})
	# print str("-----------根据网站查询----------").decode("utf-8")
	# for item in result:
	# 	item.show_account()

	# result = manager.search_account({"tag":["hot", "interesting"]})
	# print str("----------根据标签查询----------").decode("utf-8")
	# for item in result:
	# 	item.show_account()

	# result = manager.search_account({"sign":"DB", "tag":["hot"]})
	# print str("----------复合条件查询----------").decode("utf-8")
	# for item in result:
	# 	item.show_account()

if __name__ == '__main__':
	test()
