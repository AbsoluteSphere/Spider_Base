import os

import requests
import re

# 获取到当前网址上的音乐信息   MP3

#


# 获取到资源地址
url = 'https://houzi8.com/peiyue/qingyinyue-0-0-0-0-0-0/4'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
# 发送请求
response = requests.get(url, headers=headers)
print(response.text)
# 解析数据
mp3_list = re.findall(r'title:"(.*?)",.*?,preview_url:"(.*?)",wav', response.text)
# print(mp3_list)
for title, mp3_url in mp3_list:
    # sub 替换的规则  替换的内容   替换的数据
    mp3_url = 'https:' + mp3_url.replace(r'\u002F', '/')
    # print(title, mp3_url)
    res = requests.get(mp3_url, headers=headers)
    path = '铃声/'
    if not os.path.exists(path):
        os.mkdir(path)
    with open(path + title + '.mp3', 'wb')as f:
        f.write(res.content)
# 保存数据

