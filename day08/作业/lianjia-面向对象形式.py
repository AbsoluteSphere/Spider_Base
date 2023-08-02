# xpath语法
import requests
from lxml import etree


class Lianjia:
    # 获取资源地址
    def __init__(self):
        self.url = 'https://sh.lianjia.com/ershoufang/pudong/pg2/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

    # 发送请求获取数据
    def get_data(self):
        response = requests.get(self.url, headers=self.headers)
        response.encoding = 'utf-8'
        return response.text

    # 提取数据
    def parse_data(self, res):
        html_obj = etree.HTML(res)
        li_list = html_obj.xpath('//ul[@class="sellListContent"]/li')
        item = {}
        for li in li_list:
            item['title'] = li.xpath('./div[@class="info clear"]/div[@class="title"]/a/text()')[0]
            region_1 = li.xpath('./div[@class="info clear"]/div[@class="flood"]/div[@class="positionInfo"]/a[1]/text()')
            region_2 = li.xpath('./div[@class="info clear"]/div[@class="flood"]/div[@class="positionInfo"]/a[2]/text()')
            item['region'] = '- '.join(region_1 + region_2)
            item['house_info'] = \
            li.xpath('./div[@class="info clear"]/div[@class="address"]/div[@class="houseInfo"]/text()')[0]
            item['follow_info'] = li.xpath('./div[@class="info clear"]/div[@class="followInfo"]/text()')[0]
            item['unit_price'] = li.xpath(
                './div[@class="info clear"]/div[@class="priceInfo"]/div[@class="unitPrice"]/span/text()')[0]
            item['total_price'] = ''.join(li.xpath(
                './div[@class="info clear"]/div[@class="priceInfo"]/div[@class="totalPrice totalPrice2"]/span/text()') + [
                                              '万'])
            print(item)

    # 主函数
    def main(self):
        res = self.get_data()
        self.parse_data(res)


if __name__ == '__main__':
    lian = Lianjia()
    lian.main()