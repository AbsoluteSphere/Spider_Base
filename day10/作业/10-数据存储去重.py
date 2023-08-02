'''
获取搜狐视频电影一栏里的电视剧信息，提取名称、周播放数、主演，获取10个页面，将数据分别存储在mysql和MongoDB数据库,对数据进行去重,以及对请求网址实现去重
目标网址：https://so.tv.sohu.com/list_p1100_p2_p3_p4_p5_p6_p7_p8_p9_p102_p11_p12_p13_p14.html
'''
import requests
from lxml import etree
import pymysql
import pymongo
import redis
import hashlib


class Souhu:
    def __init__(self):
        # mysql数据库初始化
        self.db = pymysql.connect(host='localhost', user='root', password='123456', db='spider_mysql', port=3306)
        self.cursor = self.db.cursor()
        # mongodb数据库初始化
        self.client = pymongo.MongoClient()
        self.collection = self.client['spider_mongo']['tv']
        # redis数据库初始化
        self.redis = redis.Redis()
        self.url = 'https://so.tv.sohu.com/list_p1100_p2_p3_p4_p5_p6_p7_p8_p9_p10{}_p11_p12_p13_p14.html'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }

    def get_data(self, page):
        response = requests.get(self.url.format(page), headers=self.headers)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        else:
            print('状态码不对')

    def parse_data(self, res):
        html_object = etree.HTML(res)
        li_list = html_object.xpath("//ul[@class='st-list cfix']/li")
        for li in li_list:
            item = {}
            item['name'] = li.xpath(".//strong/a/text()")[0]
            item['number'] = li.xpath(".//p[@class='num-bf']/text()")[0] if li.xpath(
                ".//p[@class='num-bf']/text()") else ''
            item['actor'] = li.xpath(".//p[@class='actor']/a[1]/text()")[0] + '/' + \
                            li.xpath(".//p[@class='actor']/a[2]/text()")[0] if len(li.xpath(
                ".//p[@class='actor']/a[2]/text()")) else li.xpath(".//p[@class='actor']/a[1]/text()")[0] if len(
                li.xpath(".//p[@class='actor']/a[1]/text()")) else ''
            # print(item)
            # 判断当前数据是否重复
            res = self.save_data_redis(item)
            if res:
                # 用mysql存储
                self.save_data_mysql(item)
                print(f"{item['name']}mysql存储成功")
                # 用mongodb存储
                self.save_data_mongodb(item)
                print(f"{item['name']}mongodb存储成功")
            else:
                print(f"{item['name']}重复")
                continue

    # 通过哈希将数据进行加密
    def get_md5(self, value):
        # 生成一个md5加密对象
        md5 = hashlib.md5()
        md5.update(str(value).encode('utf-8'))
        return md5.hexdigest()

    # 通过redis进行数据去重
    def save_data_redis(self, item):
        value = self.get_md5(item)
        # 通过redis的集合插入sadd判断要插入是否成功,一般过滤的参数名加:filter，插入成功返回1
        return self.redis.sadd('movie:filter', value)

    # 创建mysql数据表
    def create_table_mysql(self):
        # 使用预处理语句创建表
        sql = '''
        CREATE TABLE IF NOT EXISTS souhu_movie(
                    id int primary key auto_increment not null,
                    name VARCHAR(255) NOT NULL, 
                    number VARCHAR(255) , 
                    actor VARCHAR(255)
                    )
        '''
        try:
            self.cursor.execute(sql)
            print("CREATE TABLE SUCCESS.")
        except Exception as ex:
            print(f"CREATE TABLE FAILED,CASE:{ex}")

    def save_data_mysql(self, item):
        sql = 'insert into souhu_movie(id, name, number, actor) values(%s,%s,%s,%s)'
        self.cursor.execute(sql, (0, item['name'], item['number'], item['actor']))
        self.db.commit()

    def save_data_mongodb(self, item):
        self.collection.insert_one(item)

    def main(self):
        self.create_table_mysql()
        for i in range(1, 11):
            # 对网页去重
            url_res = self.save_data_redis(self.url.format(i))
            if url_res:
                res = self.get_data(i)
                self.parse_data(res)
                print(f"************请求{self.url.format(i)}地址成功************")
            else:
                print('地址重复')
                continue


if __name__ == '__main__':
    sohu = Souhu()
    sohu.main()
