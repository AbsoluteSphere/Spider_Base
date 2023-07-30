

import requests


url = 'https://www.baidu.com/'
response = requests.get(url)
print(type(response.cookies))
print(requests.utils.dict_from_cookiejar(response.cookies))