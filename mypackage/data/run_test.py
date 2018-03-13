from base.run_method import RunMain
from get_data import GetData
from depend_data import DependData
from util.common_util import CommonUtil

class RunTest:
	"""docstring for RunTest"""
	def __init__(self):
		# 实例化http请求方法对象
		self.run_method = RunMain()
		# 实例化获取excel内容方法的对象
		self.data = GetData()
		self.com_util = CommonUtil()

	# 执行程序,遍历case（除了表头）
	def start_mycase(self):
		pass_count = []
		fail_count = []
		rows_count = self.data.get_case_lines()
		for i in range(2,rows_count+1):
			# 拿到是否执行的boolean
			is_run = self.data.get_is_run(i)
			if is_run :
				# 拿到url
				url = self.data.get_request_url(i)
				# 拿到请求类型
				request_method = self.data.get_request_method(i)
				# 拿到请求需要的json参数
				request_json = self.data.get_data_json(i)
				# 是否需要填写header
				is_header = self.data.get_is_header(i)
				# 拿到预期结果
				expected_data = self.data.get_expected_results(i)
				# 判断用例是否需要依赖别的用例
				depend_case = self.data.is_denpend(i)
				if depend_case != None:
					print(depend_case)
					print(type(depend_case))
					self.depend_data = DependData(depend_case)
					#获取依赖的响应数据
					# print(i)
					depend_response_data = self.depend_data.get_data_key(i)
					# 获取依赖的key
					depend_key = self.data.get_depend_file(i)
					# 更新依赖key的数据
					# request_json[self.depend_data] = depend_response_data
				# print("请求需要的参数:",request_json)
				# print("header:",is_header)
				res = self.run_method.run_main(url, request_method, request_json, is_header)
				# print(res)
				# if int(res_status) == 200 :
				# 	self.data.write_result(i,'pass')
				# 	pass_count.append(i)
				# 	# print('成功执行')
				# else:	
				# 	self.data.write_result(i,'fail')
				# 	fail_count.append(i)
					# print('成功执行')
				print(type(expected_data))
				print(type(res))
				if self.com_util.is_contain(expected_data,res):
					self.data.write_result(i,'pass')
					pass_count.append(i)
				else:
					self.data.write_result(i,res)
					fail_count.append(i)


		print('成功的个数:',len(pass_count))
		print('失败的个数:',len(fail_count))

if __name__ == '__main__':
	obj = RunTest()
	obj.start_mycase()
	# print(obj.start_mycase())