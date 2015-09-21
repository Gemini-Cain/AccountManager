#@Date 2015/09/15
#@Author Xin Du
#coding:utf-8

import json

class AccountManager(object):
	"""账户管理类"""
	def __init__(self):
		super(Account, self).__init__()
		self.name = name
		self.sign = sign
		self.website = website
		self.login_name = login_name
		self.tag = tag


	def add_account(self, account):
		for line in open(self.file):
			#line = line.decode("gbk").encode("utf-8")
			print line.decode("utf-8").encode("gbk")
			text = json.loads(line)
			for key in text.keys():
				if text[key]:
					pass
				print "[" + key + "]"
				print text[key]

	def search_account(self):
		pass

	def delete_account(self):
		pass

	def change_account(self):
		pass

