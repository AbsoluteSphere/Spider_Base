

import requests
from lxml import etree

# etree.HTML将字符串数据转换成 元素对象  element对象   element对象才具有xpath方法
# html = etree.HTML(text)
# html.xpath() # 取得的数据是一个列表


# 获取到资源地址
for i in range(1, 10):
    url = 'https://www.77xsw.cc/fenlei/1_{}/'.format(i)
    # 发送请求
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'gbk'
    # print(response.text)
    # 提取数据  将数据转换成预算对象
    html_obj = etree.HTML(response.text)
    # 如果取出的不是属性或者文本数据   那么返回的依然是元素对象  可以继续对元素对象进行xpath语法取值
    # print(html_obj.xpath('//li'))
    li_list = html_obj.xpath('//div[@id="mm_14"]/ul/li[position()>1]')
    # print(li_list)
    for li in li_list:
        # print(li)
        title = li.xpath('./span[@class="sp_2"]/a/text()')[0] if li.xpath('./span[@class="sp_2"]/a/text()') else '空'
        href = li.xpath('./span[@class="sp_2"]/a/@href')[0] if li.xpath('./span[@class="sp_2"]/a/@href') else '空'
        print(title, href)
