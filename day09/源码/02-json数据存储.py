
import requests
from lxml import etree
import json
url = 'https://www.4399.com/flash/new_5.htm'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
response.encoding = 'gbk'
html_boj = etree.HTML(response.text)
li_list = html_boj.xpath('//div[@class="bre oh"]/ul/li')
data_list = []
for li in li_list:
    item = {}
    item['href'] = li.xpath('./a/@href')[0]
    item['title'] = li.xpath('./a/b/text()')[0]
    data_list.append(item)

with open('data.json', 'w', encoding='utf-8')as f:
    f.write(json.dumps(data_list, ensure_ascii=False, indent=2))