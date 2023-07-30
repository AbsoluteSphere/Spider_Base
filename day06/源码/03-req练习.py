import requests

url = 'http://image11.m1905.cn/uploadfile/2021/0922/thumb_0_647_500_20210922030733993182.jpg'
response = requests.get(url)
print(response.content)  # 获取的数据  就行响应体的数据
with open('小姐姐.png', 'wb')as f:
    f.write(response.content)