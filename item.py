#@Date 2015/09/15
#@Author Xin Du
#coding:utf-8


class Account(object):
	"""账户信息"""
	def __init__(self, name, sign, website, login_name = {}, password = {}, tag = []):
		super(Account, self).__init__()
		self.__name = name
		self.__sign = sign
		self.__website = website
		self.__login_name = login_name
		self.__password = password
		self.__tag = tag

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
		return login_name

	def set_login_name(self, login_name):
		for key in login_name.keys():
			self.__login_name[key] = login_name[key]

	def show_account(self):
		print "="*50
		print "%-20s%30s" % ("Type", "Content")
		print "-"*50
		print "%-20s%30s" % ("[Name]", self.__name)
		print "%-20s%30s" % ("[Sign]", self.__sign)
		print "%-20s%30s" % ("[Website]", self.__website)
		if self.__login_name is not None:
			for key in self.__login_name.keys():
				print "%-20s%30s" % ("[Login Name]." + key, self.__login_name[key])
		if self.__password is not None:
			for key in self.__password.keys():
				print "%-20s%30s" % ("[Password]." + key, self.__password[key])
		if self.__tag is not None:
			for item in self.__tag:
				print "%-20s%30s" % ("[Tag]", item)
		#for item in self.__login_name:
		#	print "[%s]: "
		print "-"*50

def test():
	account = Account("test", "TT", "www.douban.com")
	login_name = {"username" : "duxin"}
	account.set_login_name(login_name)
	account.show_account()
	login_name["email"] = "duxin621@yeah.net"
	account.show_account()

if __name__ == '__main__':
	test()