

import requests


# 获取到资源地址
url = 'http://www.cninfo.com.cn/new/disclosure'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
# 发送请求  一般是没有顺序要求的
data = {
    'column': 'szse_latest',
    'pageNum': '2',
    'pageSize': '30',
    'sortName': '',
    'sortType': '',
    'clusterFlag': 'true',
}
# print(data)
# 发送post 请求
response = requests.post(url, data=data, headers=headers)
print(response.json()['classifiedAnnouncements'])