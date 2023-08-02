'''
网址:http://ip.yqie.com/ipproxy.htm
用bs4来做一个简单的爬虫，爬取某个ip网址里的免费ip，获取每个ip的代理IP地址、端口、服务器地址、是否匿名、类型、存活时间
'''
import requests
from bs4 import BeautifulSoup
url = 'http://ip.yqie.com/ipproxy.htm'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
tr_list = soup.find_all('tr')
item = {}
for tr in tr_list:
    if tr.select('td:first-child'):
        item['ip_address'] = tr.select('td:first-child')[0].getText()
        item['port'] = tr.select('td:nth-child(2)')[0].getText()
        item['server_address'] = tr.select('td:nth-child(3)')[0].getText()
        item['anonymous'] = tr.select('td:nth-child(4)')[0].getText()
        item['type'] = tr.select('td:nth-child(5)')[0].getText()
        item['survival_time'] = tr.select('td:last-child')[0].getText()
        print(item)