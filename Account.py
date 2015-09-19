#@Date 2015/09/15
#@Author Xin Du
#coding:utf-8


class Account(object):
	"""账户信息"""
	def __init__(self, name, sign, website, login_name, password, tag):
		super(Account, self).__init__()
		self.name = name
		self.sign = sign
		self.website = website
		self.login_name = login_name
		self.tag = tag

	def changeName(self, name):
		if name == self.name:
			return
		else:
			self.name = name

	def changeSign(self, sign):
		if self.sign == sign:
			return
		else:
			self.sign == sign