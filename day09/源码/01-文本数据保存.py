
import requests
from bs4 import BeautifulSoup

# 获取到资源地址
url = 'https://www.zhihu.com/explore'
# 发送请求
response = requests.get(url)
# print(response.text)
soup = BeautifulSoup(response.text, 'lxml')
a_list = soup.select('div .css-1g4zjtl a')
# print(a_list)
for a in a_list:
    title = a.get_text()
    print(title)
    # 保存数据
    with open('data.txt', 'a', encoding='utf-8')as f:
        f.write(title)
        f.write('\n')