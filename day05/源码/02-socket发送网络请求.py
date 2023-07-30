import socket
import re
# 获取到url地址
url = 'http://image11.m1905.cn/uploadfile/2021/0922/thumb_0_647_500_20210922030733993182.jpg'

# 发送请求
# 1. 创建套接字
client = socket.socket()
# 创建连接
client.connect(('image11.m1905.cn', 80))
# 构造http请求
http_req = 'GET ' + url + ' HTTP/1.0\r\nUser-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36\r\n\r\n'
# 发送请求
client.send(http_req.encode())
# 提取数据
# 获取到全部数据
result = b''
data = client.recv(1024)
# print(data)
# 循环接受数据
while data:
    result += data
    data = client.recv(1024)

# print(result)
imgs = re.findall(b'\r\n\r\n(.*)', result, re.S)
print(imgs[0])

# 保存数据
with open('小姐姐.png', 'wb')as f:
    f.write(imgs[0])


