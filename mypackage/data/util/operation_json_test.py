import json
from pprint import pprint
# 打开json文件，读取文件将JSON编码的字符串转换回一个Python数据结构
with open('/Users/jk/Desktop/ruhr.json', 'r') as f:
    data = json.load(f)
    # pprint(data['data'][0])
    yy=data['data'][0]
    print(yy)	

    for k,v in yy.items():
    	print(k,':',v)