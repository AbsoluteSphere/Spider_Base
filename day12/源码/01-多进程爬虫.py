import time

import requests
import pymongo
from multiprocessing import Process
from multiprocessing import JoinableQueue as Queue


class Tenxun():
    client = pymongo.MongoClient()
    table = client['spiders11']['tenxun']
    def __init__(self):
        self.url = 'https://pbaccess.video.qq.com/trpc.vector_layout.page_view.PageService/getPage?video_appid=3000010'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        # 保存请求参数的队列
        self.url_json_queue = Queue()
        # 保存数据的队列
        self.data_queue = Queue()
        # 保存解析之后的数据信息
        self.save_queue = Queue()

    def get_url_data(self):
        """
        获取到所有的请求传递参数

        :return:
        """
        for i in range(1, 30):
            data = {"page_context": {"page_index": str(i)},
                    "page_params": {"page_id": "channel_list_second_page", "page_type": "operation",
                                    "channel_id": "100173", "filter_params": "sort=75", "page": str(i)},
                    "page_bypass_params": {"params": {"page_id": "channel_list_second_page", "page_type": "operation",
                                                      "channel_id": "100173", "filter_params": "sort=75", "page": str(i),
                                                      "caller_id": "3000010", "platform_id": "2",
                                                      "data_mode": "default", "user_mode": "default"},
                                           "scene": "operation", "abtest_bypass_id": "216eda64f427279e"}}
            self.url_json_queue.put(data)



    def get_data(self):
        while True:
            data = self.url_json_queue.get()
            response = requests.post(self.url, headers=self.headers, json=data)
            # print(response.json())
            self.data_queue.put(response.json())
            # 把队列中的计数减一
            self.url_json_queue.task_done()

    def parse_data(self):
        """
        解析数据的函数

        :return:
        """
        while True:
            content = self.data_queue.get()
            for node in content['data']['CardList'][0]['children_list']['list']['cards']:
                item = {}
                item['second_title'] = node['params']['second_title']
                item['timelong'] = node['params'].get('timelong') if node['params'].get('timelong') else '空'
                item['publish_date'] = node['params'].get('publish_date') if node['params'].get('publish_date') else '空'
                item['epsode_pubtime'] = node['params'].get('epsode_pubtime') if node['params'].get('epsode_pubtime') else '空'
                self.save_queue.put(item)

            self.data_queue.task_done()

    def save_data(self):
        """
        保存函数
        """
        while True:
            item = self.save_queue.get()
            self.table.insert_one(item)
            print(item)
            self.save_queue.task_done()

    def main(self):
        p_list = []

        p_data = Process(target=self.get_url_data)
        p_list.append(p_data)
        # 发送请求的进程
        for i in range(2):
            p_get = Process(target=self.get_data)
            p_list.append(p_get)

        # 提取数据的进程
        for i in range(2):
            p_parse = Process(target=self.parse_data)
            p_list.append(p_parse)

        # 保存数据
        p_save = Process(target=self.save_data)
        p_list.append(p_save)
        for p in p_list:
            # 设置程序为守护主进程
            p.daemon = True
            p.start()



        time.sleep(5)
        for q in [self.url_json_queue,self.data_queue,  self.save_queue]:
            q.join()

        print('主进程结束!!!!')


if __name__ == '__main__':
    tx = Tenxun()
    tx.main()
