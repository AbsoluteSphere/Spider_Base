
import requests
# 下载命令  pip install requests

# 目标的url
url = 'https://www.baidu.com'

# 发送请求  发送get 请求
response = requests.get(url)

# response常见的属性
print(response.text)  # 查看文本数据  获取的是响应体的内容  字符串数据类型
print(response.content)  # 获取的是响应体的内容   bytes数据类型
print(response.status_code)  # 查看响应的状态码
print(response.request.headers)  # 查看请求头
print(response.headers)  # 查看响应头
print(response.cookies)  # 查看响应的cookie