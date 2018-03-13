import json
import unittest
import HTMLTestRunner
from demo import RunMain


class RuhrTest(unittest.TestCase):
	def setUp(self):
		self.run = RunMain()

	def test_01(self):
		find_all_station_url = 'http://192.168.1.104:8081/u/community/find/community'
		res = self.run.run_main(find_all_station_url, 'GET')
		print(id)
		print(json.dumps(res, indent=2, sort_keys=True))
		self.assertEqual(res['status'], 'success', '测试失败')


if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(RuhrTest('test_01'))
	unittest.TextTestRunner().run(suite)
