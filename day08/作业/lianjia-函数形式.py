'''
用xpath做一个简单的爬虫，爬取链家网里的租房信息获取标题，位置，房屋的格局（三室一厅），关注人数，单价，总价
'''
import requests
from lxml import etree
# 获取资源地址
url = 'https://sh.lianjia.com/ershoufang/pudong/pg2/'
# 发送请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
response.encoding = 'utf8'
# 解析数据
# print(response.text)
html = etree.HTML(response.text)
li_list = html.xpath("//ul[@class='sellListContent']/li")
item = {}
for li in li_list:
    item['title'] = li.xpath(".//div[@class='title']/a/text()")[0]
    item['position'] = li.xpath(".//div[@class='positionInfo']/a[1]/text()")[0]
    item['style'] = li.xpath(".//div[@class='houseInfo']/text()")[0]
    item['concern'] = li.xpath(".//div[@class='followInfo']/text()")[0]
    item['price'] = li.xpath(".//div[@class='unitPrice']//span/text()")[0]
    item['total'] = li.xpath(".//div[@class='totalPrice totalPrice2']//span/text()")[0]+'万'
    print(item)

