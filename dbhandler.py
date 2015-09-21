#@Date 2015/09/15
#@Author Xin Du
#coding:utf-8

import json

class DBHandler(object):
	"""Json处理"""
	def __init__(self, file):
		super(DBHandler, self).__init__()
		self.file = file
	
	def __read_json_file__(self):
		for line in open(self.file):
			#line = line.decode("gbk").encode("utf-8")
			print line.decode("utf-8").encode("gbk")
			text = json.loads(line)
			for key in text.keys():
				if isinstance(text[key], list):
					for item in text[key]:
						print type(item)
						print item
				print type(text[key])
				print "[" + key + "]"
				print text[key]
 	
 	def __writeJsonFile__(self):
		for line in open(self.file):
			#line = line.decode("gbk").encode("utf-8")
			print line.decode("utf-8").encode("gbk")
			text = json.dumps(line)
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

	def __is_exist__(self, key):
		'判断key值数据是否已经存在'
		file = open(self.file, "r")
		while True:
			line = file.readline()
			if line is None:
				break;
			for key in line:
				pass
			json_to_python = json.loads(line)

def test():
	json = DBHandler("D:\\Code\\AccountManager\\test.txt")
	json.__read_json_file__()
	#condition = {"name" : str("豆瓣").decode("utf-8"), "symbol" : str("DB").decode("utf-8")}
	#result = json.search(condition)
	#print result

if __name__ == '__main__':
	test()