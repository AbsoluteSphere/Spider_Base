import requests

session = requests.session()
url = 'http://www.cninfo.com.cn/new/disclosure'
# 1,在请求头里带上cookie字段
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}
data = {
    'column': 'szse_latest',
    'pageNum': '2',
    'pageSize': '30',
    'sortName': '',
    'sortType': '',
    'clusterFlag': 'true',
}
response = session.post(url, headers=headers, data=data)
print(response.headers)

res = session.get('http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice')
print(res.request.headers)