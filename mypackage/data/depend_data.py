from util.operation_excel import OperationExcel
from base.run_method import RunMain
from get_data import GetData
from jsonpath_rw import jsonpath, parse
import json

class DependData(object):
	
	'''有依赖的case处理模块，case2依赖case1点数据
	'''
	def __init__(self, case_id):
		self.case_id = case_id
		self.opera_excel = OperationExcel()
		self.get_data = GetData()

	# 获取目标行的数据	
	def get_case_line_data(self):
		return self.opera_excel.get_rows_data(self.case_id)

	# 执行case1用例返回结果
	def run_denpend(self):
		run_method = RunMain()
		# 执行请求
		row_num = self.opera_excel.get_rows_num(self.case_id) + 1
		# print(row_num)
		request_json = self.get_data.get_data_json(row_num)
		url = self.get_data.get_request_url(row_num)
		# print(url)
		request_method = self.get_data.get_request_method(row_num)
		is_header = self.get_data.get_is_header(row_num)
		res= run_method.run_main(url, request_method, request_json, is_header)
		# 返回请求结果
		return res

	# 在case1用例返回的数据中，拿到case2所需要的字段的数据，返回
	def get_data_key(self, row):
		depend_data_key = self.get_data.get_depend_key(row)
		# print(depend_data_key)
		# 将str数据类型转换为json数据类型（dict字典）
		response_data = json.loads(self.run_denpend())
		# print(type(response_data))
		# 需要在json中匹配的字段规则
		jsonpath_expr = parse(depend_data_key)
		# 在json数据中查找规则字段 返回一个list
		male = jsonpath_expr.find(response_data)
		# 返回需要的对应字段中的内容
		return [match.value for match in male][0]



if __name__ == '__main__':
	obj = DependData('jk-1')
	# print(obj.get_case_line_data())
	# print(obj.run_denpend())
	print(obj.get_data_key(3))
