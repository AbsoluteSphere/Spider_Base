# 需求:采集微漫画漫画图片,上传图片,和抓包抓到的数据
import os
import requests
import pymongo
import time


class Anima:
    def __init__(self):
        # 获取漫画章节列表
        self.url_chapter = 'http://api.manhua.weibo.com/client/comic/show?comic_id=67774'
        self.headers = {
            "client-ver": "3.0.1",
            "client-type": "android",
            "client-time": "1691123860370",
            "phone-mark": "FD81F39E8F49A038DBCCF534624DE701",
            "app-devicetoken": "e571dd8bd67803995b9bdcfefb58662b",
            "sina-uid": "0",
            "sina-token": "",
            "VREADREFER": "vmh_client",
            "client-sign": "861ced3f91f03187592655195cdc6496",
            "Cache-Control": "no-cache",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Host": "api.manhua.weibo.com",
            "User-Agent": "okhttp/3.8.0"
        }
        self.data = {
            "client_ver": "3.0.1",
            "client_type": "android",
            "client_time": "1691123860370",
            "phone_mark": "FD81F39E8F49A038DBCCF534624DE701",
            "app_devicetoken": "e571dd8bd67803995b9bdcfefb58662b",
            "sina_uid": "0",
            "sina_token": "",
            "client_sign": "861ced3f91f03187592655195cdc6496"
        }
        # 获取单章图片
        self.url_img = 'http://api.manhua.weibo.com/client/comic/play?chapter_id=251298'
        self.client = pymongo.MongoClient()
        self.db = self.client['spider_mongo']['anima']

    def get_url(self):
        """
        发送请求，获取漫画章节id和章节名
        :return:
        """
        res = requests.post(self.url_chapter, headers=self.headers, data=self.data)
        list = []
        for chapter in res.json()['data']['chapter_list']:
            item = {}
            item['chapter_id'] = chapter['chapter_id']
            item['chapter_name'] = chapter['chapter_name']
            # print(item)
            list.append(item)
        return list

    def get_data(self, id):
        """
        根据章节id发送请求,获取章节的返回数据
        :param id:
        :return:
        """
        response = requests.post(self.url_img.format(id), headers=self.headers, data=self.data)
        return response.json()

    def parse_data(self, res, name):
        """
        解析章节请求返回的数据，即图片地址
        :param res:
        :param name:
        :return:
        """
        list = res['data']['json_content']['page']
        for page in list:
            item = {}
            item['title'] = name + '-' + str(list.index(page))
            item['img'] = page['mobileImgUrl']
            item['index'] = str(list.index(page))
            # print(item)
            self.save_data(item, name)

    def save_data(self, item, name):
        """
        根据图片地址发送请求返回二进制数据，保存图片在文件夹中，并将解析的数据保存在MongoDB
        :param item:
        :return:
        """
        self.db.insert_one(item)
        # 创建保存图片的文件夹，如果文件夹不存在的话
        save_folder = '秘境王冠/' + name
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        save_path = os.path.join(save_folder, item['index'] + '.jpg')  # 拼接保存路径
        if os.path.exists(save_path):
            print(f"图片文件 {item['title']} 已存在，跳过保存")
        else:
            # 获取图片请求
            img_res = requests.get(item['img'])
            with open(save_path, 'wb')as f:
                # 二进制数用content获取
                f.write(img_res.content)
            print(f"图片文件 {item['title']} 保存成功")

    def main(self):
        list = self.get_url()
        for page in list:
            id = page['chapter_id']
            name = page['chapter_name']
            res = self.get_data(id)
            self.parse_data(res, name)


if __name__ == '__main__':
    anima = Anima()
    start = time.time()
    anima.main()
    end = time.time()
    print("total cost:", end - start)
