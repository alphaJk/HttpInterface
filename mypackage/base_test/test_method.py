from demo import RunMain
# import json
import unittest
import HTMLTestRunner

'''
通常情况下每一个case执行时都会执行setUp和tearDown方法
'''


class TestMethod(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     print('类执行之前的方法')
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print('类执行之后的方法')
    # 每次方法之前执行
    def setUp(self):
        # 实例化
        self.run = RunMain()

    # 每次方法之后执行
    # def tearDown(self):
    #     print('这是tearDown方法')

    # case必须以test开头
    def test_01(self):
        imooc_url = 'https://coding.imooc.com/api/cate'
        imooc_data2 = {
            'cid': '0',
            'uid': '2828275',
            'timestamp': '1516068952314',
            'token': '87f6ebcd18782552d277f3b1599fbf3d',
            'secrect': '2c977a343d356545f305e084d4aaf364',
            'uuid': 'f9f20ffa594904d672120517556f835a'
        }
        res = self.run.run_main(imooc_url, 'POST', imooc_data2)
        # print(json.dumps(res, indent=2, sort_keys=True))
        # print('---------------------')
        self.assertEqual(res['errorCode'], 1000, '测试失败')
        global uid
        uid = 2828275
        print('这是第一个case')

    # 跳过这个case不执行
    # @unittest.skip('test_02')
    def test_02(self):
        imooc_url = 'https://www.imooc.com/index/getstarlist'
        res = self.run.run_main(imooc_url, 'GET')
        # print(json.dumps(res, indent=2, sort_keys=True))
        # self.assertEqual(res['errorCode'], 1000, '测试失败')
        print('这是第二个case')


if __name__ == '__main__':
    file_path = "/Users/jk/Desktop/report.html"
    fp = open(file_path, 'wb')
    suite = unittest.TestSuite()
    # 通过addcase的顺序执行case
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    # unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'this is a report', description=u'用例执行情况：')
    runner.run(suite)
