#@Date 2015/09/15
#@Author Xin Du
#coding:utf-8

import json
import account

class DBHandler(object):
	"""Json处理"""
	def __init__(self, file_name):
		super(DBHandler, self).__init__()
		self.file_name = file_name
	
	def __read_json_file__(self):
		content = []
		file = open(self.file_name)
		while True:
			line = file.readline()
			if not line:
				break
			print "%s:%s" %(__name__, line.decode("utf-8").encode("gbk"))
			text = json.loads(line)
			content.append(text)
		return content
 	
 	def __writeJsonFile__(self, content):
 		file = open(self.file_name, 'w')
		for line in content:
			print "%s:%s" %(__name__, line)
			text = json.dumps(line)
			file.write(text + "\n")
		file.close()


	def getAccounts(self):
		accounts = []
		for line in self.__read_json_file__():
			item = account.Account()
			for key in line.keys():
				if key == "id":
					if isinstance(line[key], unicode):
						item.set_id(line[key])
					else:
						raise TypeError
				if key == "name":
					if isinstance(line[key], unicode):
						item.set_name(line[key])
					else:
						raise TypeError
				elif key == "sign":
					if isinstance(line[key], unicode):
						item.set_sign(line[key])
					else:
						raise TypeError
				elif key == "website":
					if isinstance(line[key], unicode):
						item.set_website(line[key])
					else:
						raise TypeError
				elif key == "login_name":
					if isinstance(line[key], dict):
						item.set_login_name(line[key])
					else:
						raise TypeError
				elif key == "password":
					if isinstance(line[key], dict):
						item.set_password(line[key])
					else:
						raise TypeError
				elif key == "tag":
					if isinstance(line[key], list):
						item.set_tag(line[key])
					else:
						raise TypeError
				else:
					continue
			accounts.append(item)
		return accounts

	def saveAccounts(self, accounts):
		content = []
		for item in accounts:
			line = {}
			line["id"] = item.get_id();
			line["name"] = item.get_name();
			line["sign"] = item.get_sign();
			line["website"] = item.get_website();
			line["tag"] = item.get_tag();
			line["login_name"] = item.get_login_name();
			line["password"] = item.get_password();
			content.append(line)
		self.__writeJsonFile__(content)


def test():
	json = DBHandler("D:\\Code\\AccountManager\\test.txt")
	for item in json.getAccounts():
		item.show_account()

	json.saveAccounts(json.getAccounts())
	#condition = {"name" : str("豆瓣").decode("utf-8"), "symbol" : str("DB").decode("utf-8")}
	#result = json.search(condition)
	#print result

if __name__ == '__main__':
	test()