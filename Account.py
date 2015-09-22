#@Date 2015/09/15
#@Author Xin Du
#coding:utf-8


class Account(object):
	"""账户信息"""
	def __init__(self, name, sign, website, login_name = [], password = [], tag = []):
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
		return self.__login_name

	def set_login_name(self, login_name):
		self.__login_name.clear()
		for key in login_name:
			self.__login_name[key] = login_name[key]

	def get_password(self):
		return self.__password

	def set_password(self, password):
		self.__password.clear()
		for key in password:
			self.__password[key] = password[key]

	def get_tag(self):
		return self.__tag

	def set_tag(self, tag):
		self.__tag.clear()
		for item in tag:
			self.__tag.append(item)

	def show_account(self):
		print "=" * 60
		print "%-30s%30s" % ("Type", "Content")
		print "-" * 60
		print "%-30s%30s" % ("[Name]", self.__name.encode("gbk"))
		print "%-30s%30s" % ("[Sign]", self.__sign)
		print "%-30s%30s" % ("[Website]", self.__website)
		if self.__login_name is not None:
			for key in self.__login_name.keys():
				print "%-30s%30s" % ("[Login Name]." + key, self.__login_name[key])
		if self.__password is not None:
			for key in self.__password.keys():
				print "%-30s%30s" % ("[Password]." + key, self.__password[key])
		if self.__tag is not None:
			for item in self.__tag:
				print "%-30s%30s" % ("[Tag]", item)
		#for item in self.__login_name:
		#	print "[%s]: "
		print "-" * 60

def test():
	account = Account(str("豆瓣").decode("utf-8"), "DB", "www.douban.com")
	login_name = {"username" : "duxin"}
	account.set_login_name(login_name)
	account.show_account()
	account.get_login_name()["email"] = "duxin621@yeah.net"
	account.show_account()

if __name__ == '__main__':
	test()