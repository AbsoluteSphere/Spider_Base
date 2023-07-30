
import requests
# 获取到url  目标地址
# url = 'https://www.sogou.com/web?query=python'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
# response = requests.get(url, headers=headers)
# print(response.text)


# 第二种  键值对传参
url = 'https://www.sogou.com/web'
kw = {
    'query': '鸡蛋',
    '_ast': '1685882346',
    '_asf': 'www.sogou.com',
    'w': '01029901',
    'cid': '',
    's_from': 'result_up',
    'sut': '636',
    'sst0': '1685882657710',
    'lkt': '0,0,0',
    'sugsuv': '1683806424790897',
    'sugtime': '1685882657710',
}
response = requests.get(url, params=kw, headers=headers)
print(response.text)