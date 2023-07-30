import pymongo
import requests
# pip install redis
import redis
# 哈希加密算法
import hashlib





class Mgtv():
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.collection = self.client['spiders11']['mgtv']
        self.red = redis.Redis()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.url = 'https://pianku.api.mgtv.com/rider/list/pcweb/v3'

    def get_data(self, page):
        params = {
            'allowedRC': '1',
            'platform': 'pcweb',
            'channelId': '2',
            'pn': '3',
            'pc': '80',
            'hudong': '1',
            '_support': '10000000',
            'kind': '19',
            'area': '10',
            'year': 'all',
            'chargeInfo': 'a1',
            'sort': 'c2',
        }
        response = requests.get(self.url, headers=self.headers, params=params)
        if response.status_code == 200:
            if response.json()['data']['hitDocs']:
                return response.json()
            else:
                print('当前数据返回的不对,检查网站是否还有数据')
        else:

            print('状态码不对')

    def parse_data(self, response):
        for node in response['data']['hitDocs']:
            item = {}
            item['story'] = node['story']
            item['subtitle'] = node['subtitle']
            item['title'] = node['title']
            self.save_data(item)

    # 通过哈希将数据进行加密 速度会更快一些
    def get_md5(self, val):
        # 生成一个md5加密对象
        md5 = hashlib.md5()
        md5.update(str(val).encode('utf-8'))
        # print(len(md5.hexdigest()))
        return md5.hexdigest()

    def save_data(self, item):
        value = self.get_md5(item)
        res = self.red.sadd('mg:filter', value)
        if res:
            self.collection.insert_one(item)
            print('插入數據成功')
        else:
            print('数据重复!!!!')

    def main(self):
        for i in range(1, 2):
            response = self.get_data(i)
            self.parse_data(response)


if __name__ == '__main__':
    mg = Mgtv()
    mg.main()
    # mg.get_md5('1')
