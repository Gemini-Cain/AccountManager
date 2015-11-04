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
			result.append(account.Account(item["name"], item["sign"], item["website"], item["login_name"], item["password"], item["tag"]))

		return result

	def change_account(self, account):
		accounts = self.handler.getAccounts()
		for item in accounts:
			if item.get_id() == account.get_id():
				item = account
		self.handler.saveAccounts(accounts)

	def search(self, condition):
		result = []
		file = open(self.file)
		while True:
			line = file.readline()
			if not line:
				break
			is_match = True
			text = json.loads(line)
			for key in condition:
				if key in text:
					if isinstance(text[key], (str, unicode)):
						if text[key] == condition[key]:
						 	pass
						else:
							is_match = False
					elif isinstance(text[key], list):
						for item in condition[key]:
							if item in text[key]:
								pass
							else:
								is_match = False
								break
					else:
						raise TypeError
				else:
					raise KeyError
			if is_match == True:
				result.append(text)
		return result

	def insert(self, content):
		file = open(self.file, "a")
		line = json.dumps(content)
		print line
		file.write(line)

	def is_exist(self, condition):
		'判断key值数据是否已经存在'
		file = open(self.file)
		while True:
			line = file.readline()
			if not line:
				break;
			print line
			text = json.loads(line)
			print text
			for key in condition:
				if key in text and text[key] == condition[key]:
					return True
		
		return False

def test():
	manager = AccountManager()
	ac = account.Account(str("豆瓣").decode("utf-8"), "DB4", "www.douban.com", {"username" : "duxin", "mobile_phone" : "18665005621"}, {"login_password" : "123456", "pay_password" : "18665005621"}, ["hot", "interesting"])
	manager.add_account(ac)

	#manager.delete_account("9364cde347921fec50854d78f3449fc3")

	ac = account.Account(str("豆瓣").decode("utf-8"), "DB0", "www.douban.com", {"username" : "duxin", "mobile_phone" : "18665005621"}, {"login_password" : "123456", "pay_password" : "18665005621"}, ["hot", "interesting"])
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
