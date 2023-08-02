import time

import requests
import threading
import pymongo
from queue import Queue


class Aqyi():
    def __init__(self):
        self.client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        self.collection = self.client['spider']['aqy']
        self.headers = {
            'referer': 'https://list.iqiyi.com/www/2/15-------------11-1-1-iqiyi--.html?s_source=PCW_SC',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
        self.url = 'https://pcw-api.iqiyi.com/search/recommend/list?channel_id=2&data_type=1&mode=11&page_id={}&ret_num=48&session=d5dd988a618914ad25fb4c0ac47c9b29&three_category_id=15;must'
        # 存放网址的队列
        self.url_queue = Queue()
        # 存放响应数据的队列
        self.res_queue = Queue()
        # 存放保存数据的队列
        self.save_queue = Queue()

    def get_url(self):
        for i in range(1, 20):
            time.sleep(20)
            self.url_queue.put(self.url.format(i))

    def get_data(self):
        while True:
            url = self.url_queue.get()
            print(url)
            response = requests.get(url, headers=self.headers)
            self.res_queue.put(response.json())
            # 将计数减一
            self.url_queue.task_done()

    def parse_data(self):
        while True:
            data = self.res_queue.get()
            for node in data['data']['list']:
                item = {}
                item['title'] = node['title']
                item['playUrl'] = node['playUrl']
                item['description'] = node['description']
                self.save_queue.put(item)
            self.res_queue.task_done()

    def save_data(self):
        while True:
            item = self.save_queue.get()
            print(item)
            self.collection.insert_one(item)
            self.save_queue.task_done()

    def main(self):
        t_list = []
        # 线程传的是个引用地址，不是调用，不要()
        t_url = threading.Thread(target=self.get_url)
        t_list.append(t_url)
        for i in range(3):
            t_get = threading.Thread(target=self.get_data)
            t_list.append(t_get)
        for i in range(2):
            t_parse = threading.Thread(target=self.parse_data)
            t_list.append(t_parse)
        t_save = threading.Thread(target=self.save_data)
        t_list.append(t_save)
        for t in t_list:
            t.setDaemon(True)  # 设置子线程守护主线程    主线程结束    子线程强制结束
            t.start()
            # print(111)


        for q in [self.url_queue, self.res_queue, self.save_queue]:
            # 查看队列的计算是否为0  如果不为0就会阻塞代码
            q.join()


if __name__ == '__main__':
    t1 = time.time()
    yk = Aqyi()
    yk.main()
    print("total cost:", time.time() - t1)
