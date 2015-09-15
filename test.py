#@Date 2015/09/15
#@Author Xin Du
#coding:utf-8

import json

class DataHandler(object):
	"""Json处理"""
	def __init__(self, file):
		super(Json, self).__init__()
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
		result = null
		flag = True
		for line in open(self.file):
			#print line.decode("utf-8").encode("gbk")
			text = json.loads(line)
			for key in condition.keys():
				if text[key] == condition[key]:
					pass
				else:
					flag = False
					break
			if flag == True:
				result = line
				break

		return result

	def insert(self, key, content):
		for line in open(self.file):
			#line = line.decode("gbk").encode("utf-8")
			print line.decode("utf-8").encode("gbk")
			text = json.loads(line)
			for key in text.keys():
				if text[key]:
					pass
				print "[" + key + "]"
				print text[key]

def test():
	json = Json("D:\\Code\\AccountManager\\test.txt")
	json.readJson()

if __name__ == '__main__':
	test()#@Date 2015/09/15
#@Author Xin Du
#coding:utf-8

import json

class Json(object):
	"""Json处理"""
	def __init__(self, file):
		super(Json, self).__init__()
		self.file = file
	
	def readJson(self):
		for line in open(self.file):
			#line = line.decode("gbk").encode("utf-8")
			print line.decode("utf-8").encode("gbk")
			text = json.loads(line)
			for key in text.keys():
				print "[" + key + "]"
				print text[key]
 	
def test():
	json = Json("D:\\Code\\AccountManager\\test.txt")
	json.readJson()

if __name__ == '__main__':
	test()