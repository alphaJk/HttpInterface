import json
from pprint import pprint


class OperationJson(object):
	"""docstring for OperationJson
		读取json方法封装
	"""

	def __init__(self):
		# self.file_path = '/Users/jk/Desktop/ruhr.json'
		self.file_path = '/Users/jk/www/interface/mypackage/data_config/user.json'
		self.data = self.read_json()
		
	# 读取json文件方法
	def read_json(self):
		with open(self.file_path,'r') as f :
			data = json.load(f)
			return data
	# 根据关键字获取数据
	def get_data(self,id):
		'''
		    如果未找到， 返回None
		'''
		try:
			return self.data[id]
		except Exception as e:
			# print('没有在json中找到对应的关键字')
			return ''
			# raise
		 


# if __name__ == '__main__':
# 	# path = '/Users/jk/Desktop/ruhr.json'
# 	opjson = OperationJson()
# 	pprint(opjson.get_data('data'))

