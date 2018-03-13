import requests
from pprint import pprint


class RunMain(object):
    '''
        post和get方法封装
    '''
    # def __init__(self, url, method, data=None):
        # 构造函数，被实例化时就执行，参数data使用对是默认参数
        # self.res = self.run_main(url, method, data)

    def send_post(self, url, data):
        res = requests.post(url=url, data=data).json()
        return res

    def send_get(self, url, data):
        res = requests.get(url=url, data=data).json()
        return res

    def run_main(self, url, method, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res


# if __name__ == '__main__':
#     imooc_url = 'https://www.imooc.com/index/getstarlist'
#     imooc_method = ''
#     imooc_data = ''
#     run = RunMain(imooc_url, 'GET')
#     # 实例对象中对属性
#     pprint(run.res)






# imooc_data = {
#     'token': '7e11a8ee7e9221e0f395ff8b4e1d4b65',
#     'uuid': 'f9f20ffa594904d672120517556f835a',
#     'secrect': '2c977a343d356545f305e084d4aaf364',
#     'cid': '0',
#     'timestamp': '1516068952314',
#     'ui': '2828275',
#     'sort': '0',
#     'page': '1',
#     'exclude_learned': '0'
# }
# imooc_data2 = {
#     'cid': '0',
#     'uid': '2828275',
#     'timestamp': '1516068952314',
#     'token': '87f6ebcd18782552d277f3b1599fbf3d',
#     'secrect': '2c977a343d356545f305e084d4aaf364',
#     'uuid': 'f9f20ffa594904d672120517556f835a'
# }
# imooc_url = 'https://coding.imooc.com/api/szlist'
# imooc_url2 = 'https://coding.imooc.com/api/cate'
# 参数url和data发送post请求


# def send_post(url, data):
#     res = requests.post(url=url, data=data).json()
#     # 对返回对数据格式化
#     return json.dumps(res, indent=2, sort_keys=True)
#
#
# # print(send_post(imooc_url, imooc_data))
# print(send_post(imooc_url2, imooc_data2))
