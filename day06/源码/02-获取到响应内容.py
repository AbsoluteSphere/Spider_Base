
import requests
# 下载命令  pip install requests

# 目标的url
url = 'https://www.baidu.com'

# 发送请求  发送get 请求
response = requests.get(url)
response.encoding = 'utf-8'
print(response.text)
print(response.content.decode('utf-8'))

# json数据
# json()  将json 数据转换成字典数据
print(response.json())