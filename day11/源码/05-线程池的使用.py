import requests
import pymysql
from concurrent.futures import ThreadPoolExecutor
import pymongo


class Baidu():
    def __init__(self):
        self.db = pymysql.connect(host='127.0.0.1', user='root', password='root', db='spiders11')
        self.cursor = self.db.cursor()
        self.client = pymongo.MongoClient()
        self.table = self.client['spiders11']['baidu']
        self.url = 'https://talent.baidu.com/httservice/getPostListNew'
        self.headers = {
            'Referer': 'https://talent.baidu.com/jobs/social-list?search=python',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }

    def get_data(self, page):
        data = {
            'recruitType': 'SOCIAL',
            'pageSize': '10',
            'keyWord': 'python',
            'curPage': str(page),
            'projectType': ''
        }
        response = requests.post(self.url, headers=self.headers, data=data)
        return response.json()

    def parse_data(self, response):
        for node in response['data']['list']:
            item = {}
            item['name'] = node['name']
            item['workPlace'] = node['wZworkPlace']
            item['serviceCondition'] = node['serviceCondition']
            self.save_Data(item)

    def save_Data(self, item):
        print(item)
        self.table.insert_one(item)

    def main(self):
        with ThreadPoolExecutor(max_workers=5) as pool:
            for i in range(1, 10):
                response = pool.submit(self.get_data, i)
                # print(response.result())
                pool.submit(self.parse_data, response.result())


if __name__ == '__main__':
    bd = Baidu()
    bd.main()
