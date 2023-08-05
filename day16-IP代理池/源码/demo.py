from lxml import etree

import requests

url = 'http://www.amazon.cn/s?rh=n%3A2152158051&fs=true'
headers = {
            "Referer": "https://www.amazon.cn/ref=nav_logo",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "downlink": "10",
            "ect": "4g",
            "rtt": "200",
            'cookie': 'session-id=457-2191854-6593800; session-id-time=2082787201l; i18n-prefs=CNY; csm-hit=tb:s-E3YFF314HX4576WGT47N|1688050111386&t:1688050111387'
        }
proxies = {'https': 'https://120.34.241.184:20286'}
proxy_auth = requests.auth.HTTPProxyAuth('1641324821', 'cixv0obv')
res = requests.get(url, headers=headers, proxies=proxies, verify=False, auth=proxy_auth)
print(res.text)
html = etree.HTML(res.text)
print(html.xpath('//div[@class="sg-col-inner"]/span/div[1]/div/div/div//h2/a/@href'))
# print(res.content.decode('utf-8'))
# from loguru import logger
#
# logger.info('Start print log')
# logger.debug('Do something')
# logger.warning('Something maybe fail.')
# logger.info('Finish')



