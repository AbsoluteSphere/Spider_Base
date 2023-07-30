import requests
from lxml import etree

# etree.HTML将字符串数据转换成 元素对象  element对象   element对象才具有xpath方法
# html = etree.HTML(text)
# html.xpath() # 取得的数据是一个列表


# 获取到资源地址
url = 'https://www.77xsw.cc/fenlei/1_3/'
# 发送请求
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
response.encoding = 'gbk'
# print(response.text)
# 提取数据  将数据转换成预算对象
html_obj = etree.HTML(response.text)
# 将元素对象在转换成字符串
print(etree.tostring(html_obj, encoding='utf-8', method='html').decode())
# print(html_obj)
title_list = html_obj.xpath('//div[@id="mm_14"]/ul/li[position()>1]/span[@class="sp_2"]/a/text()')
href_list = html_obj.xpath('//div[@id="mm_14"]/ul/li[position()>1]/span[@class="sp_2"]/a/@href')
# # print(title_list)
# # print(href_list)
for title, href in zip(title_list, href_list):
    print(title, href)