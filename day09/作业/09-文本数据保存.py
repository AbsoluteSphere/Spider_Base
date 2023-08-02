'''网址:https://ljgk.envsc.cn/
需求：获取到地址（address），公司名字（ps_name），创建的时间（create_time），将数据分别保存在json文件和csv表格'''
import csv
import json

import requests


class Company:
    def __init__(self):
        self.data_list = []
        self.url = 'https://ljgk.envsc.cn/OutInterface/GetPSList.ashx?regionCode=0&psname=&SystemType=C16A882D480E678F&sgn=380ab28d361735734635b1ad775ecf1d10b559b1&ts=1690786548531&tc=94707242'
        self.headers = {
            'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36 (KHTML, likeGecko) Chrome / 114.0.0.0 Safari / 537.36'
        }

    def get_data(self):
        response = requests.get(self.url, headers=self.headers)
        return response.json()

    def parse_data(self, response):
        for i in response:
            item = {}
            item['address'] = i['address']
            item['ps_name'] = i['ps_name']
            item['create_time'] = i['create_time']
            self.data_list.append(item)
        return self.data_list

    # 保存为JSON格式
    def save_data_json(self, data):
        with open('company.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=2))

    # 保存为CSV格式
    def save_data_csv(self, data):
        with open('company.csv', 'a', newline='') as f:
            fi_name = ['address', 'ps_name', 'create_time']
            # f是文件对象,fieldnames是文件字段
            csv_f = csv.DictWriter(f, fieldnames=fi_name)
            csv_f.writeheader()
            for i in data:
                csv_f.writerow(i)

    def main(self):
        res = self.get_data()
        data = self.parse_data(res)
        # 保存为JSON格式
        self.save_data_json(data)
        # 保存为CSV格式
        self.save_data_csv(data)


if __name__ == '__main__':
    company = Company()
    company.main()
