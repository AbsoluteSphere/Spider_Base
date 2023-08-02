'''
网址:https://talent.baidu.com/jobs/social-list?search=python
需求:通过多线程队列的方式采集,标题,工作地址,岗位需求,将数据保存在mysql里
'''

import requests
import threading
import pymysql
from queue import Queue


class Work:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='123456', db='spider_mysql', port=3306)
        self.cursor = self.db.cursor()
        self.url = 'https://talent.baidu.com/httservice/getPostListNew'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Cookie': 'BIDUPSID=00EC204F2D476AC0401F566D0F22901D; PSTM=1675042284; BAIDUID=00EC204F2D476AC0F23CC352D54529EE:FG=1; BDUSS=msySVRmN2F5bVktfkpPaDNDcW1icEp3STd6UGhXei01WFZ-VXN2UXVZbG1iWlZrSVFBQUFBJCQAAAAAAAAAAAEAAACsPkw1ZnhwMjAxNTEwNwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGbgbWRm4G1kd; BDUSS_BFESS=msySVRmN2F5bVktfkpPaDNDcW1icEp3STd6UGhXei01WFZ-VXN2UXVZbG1iWlZrSVFBQUFBJCQAAAAAAAAAAAEAAACsPkw1ZnhwMjAxNTEwNwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGbgbWRm4G1kd; BAIDUID_BFESS=00EC204F2D476AC0F23CC352D54529EE:FG=1; ZFY=LtzSgo8lInSZ:ABG2F:AIexPrOEynLi17tfkKHUxQPO7k:C; Hm_lvt_50e85ccdd6c1e538eb1290bc92327926=1689127005,1690765932; Hm_lpvt_50e85ccdd6c1e538eb1290bc92327926=1690776677; RT="z=1&dm=baidu.com&si=c8dfe4ea-2530-4ade-a29e-f903f1f6bc78&ss=lkqdgaaa&sl=4&tt=1j1&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=kw6"',
            'Referer': 'https://talent.baidu.com/jobs/social-list?search=python'
        }
        # 存放网址载荷的队列
        self.url_queue = Queue()
        # 存放响应数据的队列
        self.res_queue = Queue()
        # 存放保存数据的队列
        self.save_queue = Queue()

    def create_table(self):
        sql = '''
                CREATE TABLE IF NOT EXISTS baidu_employ(
                    id int auto_increment primary key not null,
                    name VARCHAR(255) NOT NULL,
                    workPlace VARCHAR(255) NOT NULL,
                    serviceCondition VARCHAR(1000) NOT null)
            '''
        try:
            self.cursor.execute(sql)
            print("CREATE TABLE SUCCESS.")
        except Exception as ex:
            print(f"CREATE TABLE FAILED,CASE:{ex}")

    def get_url(self):
        for i in range(1, 11):
            data = {
                'recruitType': 'SOCIAL',
                'pageSize': '10',
                'keyWord': 'python',
                'curPage': str(i),
                'projectType': ''
            }
            self.url_queue.put(data)

    def get_data(self):
        while True:
            payload = self.url_queue.get()
            response = requests.post(self.url, headers=self.headers, data=payload)
            self.res_queue.put(response.json())
            self.url_queue.task_done()

    def parse_data(self):
        while True:
            res = self.res_queue.get()
            for node in res['data']['list']:
                item = {}
                item['name'] = node['name']
                item['workPlace'] = node['workPlace']
                item['serviceCondition'] = node['serviceCondition']
                self.save_queue.put(item)
            self.res_queue.task_done()

    def save_data(self):
        while True:
            item = self.save_queue.get()
            # print(item['name'], '*******', item['workPlace'], '*******', item['serviceCondition'])
            sql = 'INSERT INTO baidu_employ(id, name, workPlace, serviceCondition) values(%s, %s, %s, %s)'
            try:
                self.cursor.execute(sql, (0, item['name'], item['workPlace'], item['serviceCondition']))
                # 提交
                self.db.commit()
            except Exception as e:
                print('保存失败', e)
                self.db.rollback()
            self.save_queue.task_done()

    def main(self):
        self.create_table()
        t_list = []
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
            t.setDaemon(True)
            t.start()
        for q in [self.url_queue, self.res_queue, self.save_queue]:
            # 查看队列的计算是否为0  如果不为0就会阻塞代码
            q.join()


if __name__ == '__main__':
    work = Work()
    work.main()
