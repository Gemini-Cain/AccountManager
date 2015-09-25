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
		result = []
		file = open(self.file)
		while True:
			line = file.readline()
			if not line:
				break
			is_match = True
			text = json.loads(line)
			for key in condition:
				if key in text:
					if isinstance(text[key], (str, unicode)):
						if text[key] == condition[key]:
						 	pass
						else:
							is_match = False
					elif isinstance(text[key], list):
						for item in condition[key]:
							if item in text[key]:
								pass
							else:
								is_match = False
								break
					else:
						raise TypeError
				else:
					raise KeyError
			if is_match == True:
				result.append(text)
		return result

	def insert(self, content):
		file = open(self.file, "a")
		line = json.dumps(content)
		print line
		file.write(line)

	def is_exist(self, condition):
		'判断key值数据是否已经存在'
		file = open(self.file)
		while True:
			line = file.readline()
			if not line:
				break;
			print line
			text = json.loads(line)
			print text
			for key in condition:
				if key in text and text[key] == condition[key]:
					return True
		
		return False
				

def test():
	json = DBHandler("D:\\Code\\AccountManager\\test.txt")
	json.__read_json_file__()
	#condition = {"name" : str("豆瓣").decode("utf-8"), "symbol" : str("DB").decode("utf-8")}
	#result = json.search(condition)
	#print result

if __name__ == '__main__':
	test()