#@Date 2015/09/15
#@Author Xin Du
#coding:utf-8

import json

class DataHandler(object):
	"""Json处理"""
	def __init__(self, file):
		super(DataHandler, self).__init__()
		self.file = file
	
	def __readJsonFile__(self):
		for line in open(self.file):
			#line = line.decode("gbk").encode("utf-8")
			print line.decode("utf-8").encode("gbk")
			text = json.loads(line)
			for key in text.keys():
				if text[key]:
					pass
				print "[" + key + "]"
				print text[key]
 	
 	def __writeJsonFile__(self):
		for line in open(self.file):
			#line = line.decode("gbk").encode("utf-8")
			print line.decode("utf-8").encode("gbk")
			text = json.loads(line)
			for key in text.keys():
				if text[key]:
					pass
				print "[" + key + "]"
				print text[key]

	def search(self, condition):
		result = None
		flag = True
		for line in open(self.file):
			flag = True
			#print line.decode("utf-8").encode("gbk")
			line = line.decode("utf-8").encode("utf-8")
			text = json.loads(line)
			for key in condition.keys():
				print key
				if key in text.keys():
					print text[key]
				else:
					flag = False
					break
				print condition[key]
				if text[key] == condition[key]:
					pass
				else:
					flag = False
					break
			if flag == True:
				result = text
				break

		return result

	def insert(self, key, content):
		for line in open(self.file):
			#line = line.decode("gbk").encode("utf-8")
			print line.decode("utf-8").encode("utf-8")
			text = json.loads(line)
			for key in text.keys():
				if text[key]:
					pass
				print "[" + key + "]"
				print text[key]

def test():
	json = DataHandler("D:\\Code\\AccountManager\\test.txt")
	condition = {"name" : str("豆瓣").decode("utf-8"), "symbol" : str("DB").decode("utf-8")}
	result = json.search(condition)
	print result

if __name__ == '__main__':
	test()