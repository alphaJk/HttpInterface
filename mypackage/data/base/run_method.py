import requests
from pprint import pprint
import json


class RunMain(object):
	'''
	http请求封装
	'''
	def send_post(self, url, data=None, header=None):
		res = None
		if header != None:
			res = requests.post(url=url, data=data, headers=header, verify=True)
		else:
			res = requests.post(url=url, data=data, verify=True)
		# print(res.status_code)
		# return res.json(),res.status_code
		return res.json()
		# return res.status_code
		# 
	def send_get(self, url, data=None, header=None):
		res = None
		if header != None:
			res = requests.get(url=url, data=data, headers=header, verify=True)
		else:
			res = requests.get(url=url, data=data, verify=True)
		# print(res.status_code)	
		# return res.json(),res.status_code
		return res.json()
		
	def send_delete(self, url, data=None, header=None):
		res = None
		if header != None:
			res = requests.delete(url=url, data=data, headers=header)
		else:
			res = requests.delete(url=url, data=data)
		# return res.json(),res.status_code
		return res.json()

	def run_main(self, url, method, data=None, header=None):
		res = None
		if method == 'get':
			res = self.send_get(url, data, header)
		elif method == 'post':
			res = self.send_post(url, data, header)
		elif method == 'delete':
			res = self.send_delete(url, data, header)

		return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
		# return json.dumps(res,ensure_ascii=False)


(if __name__ == '__main__':)
	obj = RunMain()
	print(obj.send_post('http://www.ruhrtec.cn/tenants.do', 'post'))