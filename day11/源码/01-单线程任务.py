import time

import requests
import pymongo

# 快  稳

class Aqiyi(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        self.collection = self.client['spider']['aqy']
        self.headers = {
            'referer': 'https://list.iqiyi.com/www/2/15-------------11-1-1-iqiyi--.html?s_source=PCW_SC',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
        self.url = 'https://pcw-api.iqiyi.com/search/recommend/list'


    def get_data(self, params):
        response = requests.get(self.url, headers=self.headers, params=params)
        return response.json()

    def parse_data(self, data):
        categoryVideos = data['data']['list']
        for video in categoryVideos:
            item = {}
            item['title'] = video['title']
            item['playUrl'] = video['playUrl']
            item['description'] = video['description']
            print(item)
            self.save_data(item)

    def save_data(self, item):
        self.collection.insert_one(item)


    def main(self):
        for page in range(1, 20):
            params = {
                'channel_id': '2',
                'data_type': '1',
                'mode': '11',
                'page_id': page,
                'ret_num': '48',
                'session': 'fc7d98794f15b224b169d328bf8f9f13',
                'three_category_id': '15;must',
            }
            data = self.get_data(params)
            self.parse_data(data)



if __name__ == '__main__':
    t1 = time.time()
    yk = Aqiyi()
    yk.main()
    print("total cost:", time.time() - t1)