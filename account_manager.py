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
		result = []
		for item in self.handler.search(condition):
			result.append(account.Account(item["name"], item["sign"], item["website"], item["login_name"], item["password"], item["tag"]))

		return result


	def delete_account(self):
		pass

	def change_account(self):
		pass

def test():
	manager = AccountManager()
	#ac = account.Account(str("豆瓣").decode("utf-8"), "DB", "www.douban.com", {"username" : "duxin", "mobile_phone" : "18665005621"}, {"login_password" : "123456", "pay_password" : "18665005621"}, ["hot", "interesting"])
	#manager.add_account(ac)

	result = manager.search_account({"name":str("豆瓣").decode("utf-8")})
	print str("----------根据名称查询----------").decode("utf-8")
	for item in result:
		item.show_account()

	result = manager.search_account({"sign":"DB"})
	print str("----------根据符号查询----------").decode("utf-8")
	for item in result:
		item.show_account()

	result = manager.search_account({"website":"www.douban.com"})
	print str("-----------根据网站查询----------").decode("utf-8")
	for item in result:
		item.show_account()

	result = manager.search_account({"tag":["hot", "interesting"]})
	print str("----------根据标签查询----------").decode("utf-8")
	for item in result:
		item.show_account()

	result = manager.search_account({"sign":"DB", "tag":["hot"]})
	print str("----------复合条件查询----------").decode("utf-8")
	for item in result:
		item.show_account()

if __name__ == '__main__':
	test()
