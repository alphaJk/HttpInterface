

class CommonUtil(object):
	"""docstring for CommonUtil"""
	def is_contain(self, str_one, str_two):
		# 判断是否包含
		# return str1 in str2
		flag = None
		# 类型转换？
		# if isinstance(str_one,unicode):
		# 	str_one = str_one.encode('unicode-escape').decode('string_escape')
		# return cmp(str_one,str_two)
		if str_one in str_two:
			flag = True
		else:
			flag = False
		return flag