class global_var:
	'''
	记录每个内容所在的列数
	'''

	# case_id
	Id = '1'
	request_name = '2'
	url = '3'
	# 是否执行
	run = '4'
	request_type = '5'
	# 是否携带header
	header = '6'
	# 依赖的case
	case_depend = '7'
	# 依赖case的数据字段
	data_depend = '8'
	# 使用依赖数据的cases的数据字段
	field_depend = '9'
	# 请数据
	data = '10'
	# 预期结果
	expect = '11'
	# 结果
	result = '12'


# 获取case_id
def get_id():
    return global_var.Id

# 获取url
def get_url():
	return global_var.url

# 获取是否运行
def get_run():
	return global_var.run

def get_run_type():
	return global_var.request_type

# 是否携带header
def get_header():
	return global_var.header

def get_case_depend():
	return global_var.case_depend

def get_data_depend():
	return global_var.data_depend

def get_field_depend():
	return global_var.field_depend

def get_data():
	return global_var.data

def get_expect():
	return global_var.expect

def get_result():
	return global_var.result

# header的内容
def get_header_value():
	header={
		"from":'app',
		"name":"hpjx"
	}
	return header



	
