# 导入操作excel模块
from util.operation_excel import OperationExcel
import data_config
from util.operation_json import OperationJson

class GetData(object):
	def __init__(self):
		self.opera_excel = OperationExcel()
		self.json_data = OperationJson()
	# 获取excel的行数，就是case的数量
	def get_case_lines(self):
		return self.opera_excel.get_rows()

	# 获取是否执行参数,循环行数，输入列数
	def get_is_run(self,row):
		flag = None
		col = int(data_config.get_run())
		is_run = self.opera_excel.get_value(row, col)
		if is_run == 'yes':
			flag = True
		else:
			flag = False
		return flag

	#获取是否需要header参数
	def get_is_header(self,row):
		col = int(data_config.get_header())
		is_header = self.opera_excel.get_value(row, col)
		if is_header == 'yes':
			# 写死在data_config模块中
			return data_config.get_header_value()
		else:
			return None
	
	# 获取请求方式
	def get_request_method(self,row):
		col = int(data_config.get_run_type())
		request_method  = self.opera_excel.get_value(row, col)
		return request_method

	# 获取url
	def get_request_url(self,row):
		col = int(data_config.get_url())
		request_url = self.opera_excel.get_value(row,col)
		return request_url

	# 获取请求数据的关键字字段
	def get_request_data(self,row):
		col = int(data_config.get_data())
		request_data = self.opera_excel.get_value(row,col)
		if request_data =='':
			return None
		else:
			return request_data

	# 通过获取的关键字在自定义的json中拿到对应的data数据
	def get_data_json(self,row):
		request_json_data = self.json_data.get_data(self.get_request_data(row))
		return request_json_data

	# 获得预期结果
	def get_expected_results(self,row):
		col = int(data_config.get_expect())
		expected_results = self.opera_excel.get_value(row,col)
		if expected_results =='':
			return None
		else:
			return expected_results

	# 写入结果
	def write_result(self, row, value):
			col = int(data_config.get_result())	
			self.opera_excel.revise_value(row,col,value)

	# 获取依赖数据的字段
	def get_depend_key(self, row):
		col = int(data_config.get_data_depend())	
		data = self.opera_excel.get_value(row,col)
		if data == '':
			return None
		else:
			return data

	# 判断是否需要依赖
	def is_denpend(self, row):
		col = int(data_config.get_case_depend())
		data = self.opera_excel.get_value(row,col)	
		if data == '':
			return None
		else:
			return data

	# 获取数据依赖字段
	def get_depend_file(self, row):
		col = int(data_config.get_field_depend())
		data = self.opera_excel.get_value(row,col)
		if data == None:
			return None
		else:
			return data


# if __name__ == '__main__':
# 	getdata = GetData()
# 	print(getdata.get_request_url(11))