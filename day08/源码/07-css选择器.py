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

# css  id #  class .
# select 获取的数据 也是列表
# 标签选择器
# title = soup.select('a')
# print(title)

# 类选择器
# div = soup.select('.logotop')
# print(div)

# id选择器
# div = soup.select('#footercopyright')
# print(div)

# 层级选择器
# div = soup.select('div .navigationlinknoline')
# print(div)

# 属性选择器
# a = soup.select('a[class="navigationlink"]')
# print(a)

# 伪类选择器
# li = soup.select('li:nth-child(3)')
# print(li)

# 获取标签的内容文本
title = soup.select('title')
print(title[0].get_text())
print(title[0].getText())
print(title[0].text)
print(title[0].string)

# 获取属性
a_list = soup.select('a')
for a in a_list:
    print(a.get('href'))