#@Date 2015/09/15
#@Author Xin Du
#coding:utf-8

import time
import hashlib

class Account(object):
	"""账户信息"""
	def __init__(self, id = "", name = "", sign = "", website = "", login_name = {}, password = {}, tag = []):
		if id == "":		
			super(Account, self).__init__()
			md5 = hashlib.md5()
			md5.update(str(time.time()))
			id = md5.hexdigest()
		self.__id = id
		self.__name = name
		self.__sign = sign
		self.__website = website
		self.__login_name = login_name
		self.__password = password
		self.__tag = tag

	def get_id(self):
		return self.__id

	def set_id(self, id):
		self.__id = id

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name

	def get_sign(self):
		return self.__sign

	def set_sign(self, sign):
		self.__sign = sign

	def get_website(self):
		return self.__website

	def set_website(self, website):
		self.__website = website

	def get_login_name(self):
		return self.__login_name

	def set_login_name(self, login_name):
		self.__login_name.clear()
		for key in login_name.keys():
			self.__login_name[key] = login_name[key]

	def get_password(self):
		return self.__password

	def set_password(self, password):
		self.__password.clear()
		for key in password.keys():
			self.__password[key] = password[key]

	def get_tag(self):
		return self.__tag

	def set_tag(self, tag):
		self.__tag = []
		for item in tag:
			self.__tag.append(item)

	def show_account(self):
		print "=" * 62
		print "%-30s%32s" % ("Type", "Content")
		print "-" * 62
		print "%-30s%32s" % ("[ID]", self.__id)
		print "%-30s%32s" % ("[Name]", self.__name.encode("gbk"))
		print "%-30s%32s" % ("[Sign]", self.__sign)
		print "%-30s%32s" % ("[Website]", self.__website)
		if self.__login_name is not None:
			for key in self.__login_name.keys():
				print "%-30s%32s" % ("[Login Name]." + key, self.__login_name[key])
		if self.__password is not None:
			for key in self.__password.keys():
				print "%-30s%32s" % ("[Password]." + key, self.__password[key])
		if self.__tag is not None:
			for item in self.__tag:
				print "%-30s%32s" % ("[Tag]", item)
		#for item in self.__login_name:
		#	print "[%s]: "
		print "-" * 62

def test():
	account = Account(name = str("豆瓣").decode("utf-8"), sign = "DB", website = "www.douban.com")
	login_name = {"username" : "duxin"}
	account.set_login_name(login_name)
	account.show_account()
	account.get_login_name()["email"] = "duxin621@yeah.net"
	account.show_account()

if __name__ == '__main__':
	test()