import time
import requests
from lxml import etree


# ip代理池  封

class Daili():
    def __init__(self):
        self.base_url = 'https://www.kuaidaili.com/free/inha/{}/'
        self.test_url = 'http://httpbin.org/ip'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }

    def test_ip(self):
        pass

    def get_Data(self, page):
        response = requests.get(self.base_url.format(page), headers=self.headers)
        return response.text

    def parse_data(self, response):
        html_data = etree.HTML(response)
        tr_list = html_data.xpath('//table/tbody/tr')
        dizhi = []
        for tr in tr_list:
            item = {}
            item['ip'] = tr.xpath('./td[1]/text()')[0]
            item['port'] = tr.xpath('./td[2]/text()')[0]
            dizhi.append(item)
        return dizhi


    def save_ip(self, ip_addr):
        IPS = []
        for i in ip_addr:
            proxies = {
                'http': 'http://' + i['ip'] + ":" + i['port']
            }
            # print(proxies)
            try:
                res = requests.get(self.test_url, headers=self.headers, proxies=proxies, timeout=3)
                if res.status_code == 200:
                    print(res.status_code)
                    print(res.text)
                    IPS.append(proxies)
            except Exception as e:
                print('请求超时!!!')
        print(IPS)

    def run(self):
        for i in range(1, 20):
            response = self.get_Data(i)
            ip_addr = self.parse_data(response)
            self.save_ip(ip_addr)


if __name__ == '__main__':
    dl = Daili()
    dl.run()
