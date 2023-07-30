
from bs4 import BeautifulSoup
import requests
import re

url = 'http://ip.yqie.com/ipproxy.htm'
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
response = requests.get(url, headers=headers)

# 创建一个BeautifulSoup对象
soup = BeautifulSoup(response.content.decode('utf-8'), 'lxml')
# 美化输出
# print(soup.prettify())

# fin_all 获取的数据也是列表
# 1.传字符串
# span = soup.find_all('span')
# print(span)
#
# a = soup.find_all('a')
# print(a)

# 2.传正则表达式
# a = soup.find_all(re.compile('^b'))
# print(a)
# print(a)

# 3.传列表
# a = soup.find_all(['a', 'span'])
# print(a)

# 4. keuword
a = soup.find_all(attrs={'class': 'navigationlinknoline'})
print(a)
