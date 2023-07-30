import requests
import pymongo

# 静态数据是html
# 动态数据是json


class Aqiyi():
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.collection = self.client['spiders11']['aqy']
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.url = 'https://pcw-api.iqiyi.com/search/recommend/list?channel_id=2&data_type=1&mode=11&page_id={}&ret_num=48&session=2c0d9819411010e4c4edbec03ae2333f&three_category_id=15;must'

    # 发送请求
    def get_data(self, page):
        response = requests.get(self.url.format(page), headers=self.headers)
        return response.json()

    # 提取数据
    def parse_Data(self, data):

        for node in data['data']['list']:
            item = {}
            item['name'] = node['name']
            item['description'] = node['description']
            item['playUrl'] = node['playUrl']
            item['people'] = ','.join([i['name'] for i in node['people']['main_charactor']])
            item['categories'] = ','.join(node['categories'])
            print(item)
            self.save_data(item)

    # 保存数据
    def save_data(self, item):
        # 保存数据到mongodb
        self.collection.insert_one(item)

    def main(self):
        for i in range(1, 30):
            res = self.get_data(i)
            self.parse_Data(res)


if __name__ == '__main__':
    aqy = Aqiyi()
    aqy.main()
