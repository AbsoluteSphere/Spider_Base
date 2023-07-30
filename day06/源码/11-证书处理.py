

import requests


url = 'https://yjcclm.com/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.95 Safari/537.36'}
# timeout 设置请求时间
response = requests.get(url, headers=headers, verify=False, timeout=0.1)
print(response.text)




