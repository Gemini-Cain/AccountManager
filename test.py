#@Date 2015/09/15
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