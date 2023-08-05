#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   ymx_spider.py
# Author :   柏汌
import random
import time
from loguru import logger
import requests
from lxml import etree
from queue import Queue
import threading
from retrying import retry
from feapder.network.user_agent import get
import pymysql


class Yamaxun():
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="root", db="spiders")
        self.cursor = self.db.cursor()
        # 主页所有分类的地址
        self.index_url = 'https://www.amazon.cn/nav/ajax/hamburgerMainContent?ajaxTemplate=hamburgerMainContent&pageType=Gateway&hmDataAjaxHint=1&navDeviceType=desktop&isSmile=0&isPrime=0&isBackup=false&hashCustomerAndSessionId=c108bde04b677f19f2e5d7df74ff6ce0cad515fc&languageCode=zh_CN&environmentVFI=AmazonNavigationCards%2Fdevelopment%40B6122949553-AL2_x86_64&secondLayerTreeName=apparel_shoes%2Bcomputer_office%2Bhome_kitchen%2Bbeauty_pca%2Bkindle_ebook%2Bsports_outdoor%2Bgrocery%2Bbaby_toy%2Bphones_elec%2Bjewelry_watch%2Bhome_improvement%2Bvideo_game%2Bmusical_instrument%2Bcamera&customerCountryCode=null'
        self.headers = {
            "Referer": "https://www.amazon.cn/ref=nav_logo",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "downlink": "10",
            "ect": "4g",
            "rtt": "200",
            'cookie': 'session-id=457-2191854-6593800; session-id-time=2082787201l; i18n-prefs=CNY; csm-hit=tb:s-E3YFF314HX4576WGT47N|1688050111386&t:1688050111387'
        }
        # 快代理生成的获取Ip地址的网址
        self.ip_url = 'https://dps.kdlapi.com/api/getdps/?secret_id=o5z3ocj9kv24wyq8fy67&num=1&signature=o5sld1m2q7eisa3acq4hv14u23&pt=1&sep=1'
        # 保存快代理Ip的队列
        self.ip_queue = Queue()
        # 保存分类网址的队列
        self.classify_url_queue = Queue()
        # 保存详情页面网址的队列
        self.detail_url_queue = Queue()
        # 保存数据的队列
        self.data_queue = Queue()

    def create_table(self):
        """
        创建数据库表
        :return:
        """
        # 使用预处理语句创建表
        sql = '''
                    CREATE TABLE IF NOT EXISTS yamaxun(
                        id int primary key auto_increment not null,
                        price VARCHAR(255) NOT NULL, 
                        title VARCHAR(255) NOT NULL,
                        goods_url VARCHAR(255) NOT NULL,
                        classify VARCHAR(255) NOT NULL)
                    '''
        try:
            self.cursor.execute(sql)
            print("CREATE TABLE SUCCESS.")
        except Exception as ex:
            print(f"CREATE TABLE FAILED,CASE:{ex}")

    def get_ip(self):
        """
        获取ip数据，不断的获取，当ip队列为空时读取ip,将ip数据放进队列
        :return: ip地址
        """
        while True:
            if self.ip_queue.empty():
                response = requests.get(self.ip_url)
                # print(response.text)
                self.ip_queue.put(response.text)
            else:
                continue

    # 最大重试3次，3次全部报错，才会报错
    @retry(stop_max_attempt_number=3)
    def get_data(self, url):
        """
        发送请求专用方法
        :param url:
        :return:
        """
        ip = self.ip_queue.get()
        proxies = {
            'https': 'https://' + ip,
        }
        print(proxies)
        # feapder库的get()方法获取随机ua
        self.headers['User-Agent'] = get()
        response = requests.get(url=url, headers=self.headers, timeout=2, proxies=proxies, verify=False)
        # print(response.text)
        # 让有效ip一直使用
        if response.status_code == 200:
            self.ip_queue.put(ip)
        else:
            print('状态码异常')
        return response

    def get_info_url(self):
        """
        获取详情页面地址
        :return:
        """
        # 请求所有分类的网址
        response = self.get_data(self.index_url)
        html_object = etree.HTML(response.json()['data'])
        # 前两个没有请求地址
        li_list = html_object.xpath('//ul/li[position() > 2]')
        for li in li_list:
            # print(li.xpath('./a/text()'))
            item = {}
            if li.xpath('./a/text()'):
                # 全部分类的数据是分类页面
                if '全部' in li.xpath('./a/text()')[0]:
                    continue
                # 带有https的为广告页面
                if 'http' in li.xpath('./a/@href')[0]:
                    continue

                item['title'] = li.xpath('./a/text()')[0]
                item['href'] = li.xpath('./a/@href')[0].split('=')[1].split('&')[0]
                print(item)
                self.classify_url_queue.put(item)

    def detail_url_get(self):
        """
        获取详细页面数据
        :return:
        """
        while True:
            info_url = self.classify_url_queue.get()
            # time.sleep(random.randint(500, 800) / 1000)
            try:
                # 请求分类查看所有商品页面
                response = self.get_data("https://www.amazon.cn/s?rh=n%3A" + info_url['href'] + "&fs=true")
                print(response.text)
            except Exception as e:
                # 若请求三次还报错，记录错误在日志中
                logger.error("https://www.amazon.cn/s?rh=n%3A" + info_url['href'] + "&fs=true")
                continue
            html_data = etree.HTML(response.text)
            if html_data.xpath('//span[@class="s-pagination-strip"]/span[last()]/text()'):
                # 获取到分类的总共页数
                max_page = html_data.xpath('//span[@class="s-pagination-strip"]/span[last()]/text()')[0]
                for page in range(1, int(max_page) + 1):
                    # 每个分类单独页面拼接
                    new_url = 'https://www.amazon.cn/s?rh=n%3A' + info_url['href'] + '&fs=true&page=' + str(page)
                    # 请求每个分类的单独页面
                    try:
                        res = self.get_data(new_url)
                    except Exception as e:
                        # 若单独页面报错记录网址
                        logger.error('这个是请求单独页面的报错网址: ', new_url)
                        continue
                    # 若没有报错则解析里面的数据
                    html = etree.HTML(res.text)
                    detail_href_list = html.xpath('//div[@class="sg-col-inner"]/span/div[1]/div/div/div//h2/a/@href')
                    # time.sleep(random.randint(200, 500) / 1000)
                    # 获取到详情商品的详情地址和分类
                    for detail_href in detail_href_list:
                        item = {}
                        item['detail_href'] = detail_href
                        item['classify_data'] = info_url['title']

                        self.detail_url_queue.put(item)
            self.classify_url_queue.task_done()

    def paras_data(self):
        while True:
            goods_data = self.detail_url_queue.get()
            # 拼接详情页面
            goods_url = 'https://www.amazon.cn' + goods_data['detail_href']
            try:
                response = self.get_data(goods_url)
            except Exception as e:
                logger.error(goods_url)
                continue
            # print(response.text)
            html_data = etree.HTML(response.text)
            # 获取商品标题
            title = html_data.xpath('//div[@id="centerCol"]//h1/span/text()')[0] if html_data.xpath(
                '//div[@id="centerCol"]//h1/span/text()') else html_data.xpath('//title/text()')[0]
            # 获取商品价格
            if html_data.xpath('//div[@id="centerCol"]//div[@id="apex_desktop"]//span[@class="a-price-whole"]/text()'):
                price = "￥" + html_data.xpath(
                    '//div[@id="centerCol"]//div[@id="apex_desktop"]//span[@class="a-price-whole"]/text()')[0]
            else:
                price = '-'.join(html_data.xpath(
                    '//td[@class="a-span12"]//span[@class="a-offscreen"]/text()'))
            print([goods_data['classify_data'], title.strip(), price, goods_url])
            self.data_queue.put((goods_data['classify_data'], title.strip(), price, goods_url))
            self.detail_url_queue.task_done()

    def save_data(self):
        """
        保存数据
        :return:
        """
        while True:
            data_list = []
            for i in range(30):
                data = self.data_queue.get()
                # 队列存放的数据是元组,要加上一个id为了对应sql语句的占位，id是0会递增
                data_list.append((0,) + data)
                self.data_queue.task_done()

            # SQL 插入语句
            sql = 'INSERT INTO yamaxun(id, price, title, classify, goods_url) values(%s, %s, %s, %s, %s)'
            # 执行 SQL 语句
            try:
                # print(sql, (0, data[0], data[1], data[2], data[3]))
                self.cursor.executemany(sql, data_list)
                # 提交到数据库执行
                self.db.commit()
                print('数据插入成功...')
            except Exception as e:
                print(f'数据插入失败: {e}')
                # 如果发生错误就回滚
                self.db.rollback()

    def main(self):
        self.create_table()
        t_list = []
        # 获取ip线程
        t_ip = threading.Thread(target=self.get_ip)
        t_list.append(t_ip)
        # 获取主页分类线程,只请求一个网址,不需要循环创建线程
        t_info = threading.Thread(target=self.get_info_url)
        t_list.append(t_info)
        # 获取详细商品线程,有280个分类商品，每个分类下有200页数据，detail_url_get要请求5.6w次
        for i in range(7):
            t_detail_url = threading.Thread(target=self.detail_url_get)
            t_list.append(t_detail_url)
        # 解析数据线程,每页20+条数据,获取详情页面请求300w次,paras_data方法要请求300w次
        for i in range(10):
            t_paras = threading.Thread(target=self.paras_data)
            t_list.append(t_paras)
        # 保存数据线程,保存数据只需要一个线程
        t_save = threading.Thread(target=self.save_data)
        t_list.append(t_save)

        for t in t_list:
            t.setDaemon(True)
            t.start()

        time.sleep(3)
        for q in [self.classify_url_queue, self.detail_url_queue, self.detail_url_queue]:
            q.join()


if __name__ == '__main__':
    # 文件过大于500M就会重新生成一个文件
    logger.add("runtime_{time}.log", rotation="500 MB")
    ymx = Yamaxun()
    ymx.main()
