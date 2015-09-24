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

	def add_account(self, ac):
		if not isinstance(ac, account.Account):
			raise TypeError
		condition = {}
		condition["sign"] = ac.get_sign()

		if self.handler.is_exist(condition):
			raise KeyError
		else:
			condition["name"] = ac.get_name();
			print condition["name"]
			condition["website"] = ac.get_website();
			condition["tag"] = ac.get_tag();
			condition["login_name"] = ac.get_login_name();
			condition["password"] = ac.get_password();
			self.handler.insert(condition)


	def search_account(self, condition):
		for key in condition:
			if condition[key] is None or condition[key] == [] or condition[key] == "":
				del condition[key]
		return self.handler.search(condition)

	def delete_account(self):
		pass

	def change_account(self):
		pass

def test():
	manager = AccountManager()
	#ac = account.Account(str("豆瓣").decode("utf-8"), "DB", "www.douban.com", [{"type" : "username", "content" : "duxin"}, {"type" : "mobile_phone", "content" : "18665005621"}], [{"type" : "login_password", "content" : "123456"}, {"type" : "pay_password", "content" : "18665005621"}], ["hot", "interesting"])
	#manager.add_account(ac)

	result = manager.search_account({"name":str("豆瓣").decode("utf-8")})
	for item in result:
		print item

	result = manager.search_account({"sign":"DB"})
	for item in result:
		print item

	result = manager.search_account({"website":"www.douban.com"})
	for item in result:
		print item

	result = manager.search_account({"tag":["hot", "interesting"]})
	for item in result:
		print item

	result = manager.search_account({"sign":"DB", "tag":["hot"]})
	for item in result:
		print item

if __name__ == '__main__':
	test()
