import requests
import pymysql


class Ali():
    # 获取资源地址
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='root', db='spiders11')
        self.cursor = self.db.cursor()
        self.url = 'https://talent.alibaba.com/position/search?_csrf=fafa3429-541b-481f-9690-38ad369077bb'
        self.headers = {
            'Cookie': 'XSRF-TOKEN=fafa3429-541b-481f-9690-38ad369077bb; prefered-lang=zh; SESSION=RTg1REYzN0ZERkE2OERDQkJEMDUyQzZDQkI2RURCOTg=; cna=eePjHB1NR0ICAa8ANdmKpuaX; xlly_s=1; tfstk=cutFBpqh-Dne0z9-MGjygK4MUN5daRJHElWf-f4SolNix87hgsAgwOfG3OW7Q7bh.; l=fB_MxpkrNKi-t1ANBO5Z-urza77OXIOf1sPzaNbMiIEGa1rPTeCb6NC1N8d67dtjgTfmbetrip0J_dFyyja38x9_PwJbsiooVJp6-bpU-L5..; isg=BNvb7eGqO-cIsEeTbZJfY6tdaj9FsO-ylxiQz80ZyVrXrPiOVYTGA55qRgwijEeq',
            'Origin': 'https://talent.alibaba.com',
            'Referer': 'https://talent.alibaba.com/off-campus/position-list?lang=zh',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }


    # 创建数据表
    def create_table(self):
        # 使用预处理语句创建表
        sql = '''
                        CREATE TABLE IF NOT EXISTS ali(
                            id int primary key auto_increment not null,
                            workLocations VARCHAR(255) NOT NULL, 
                            name VARCHAR(255) NOT NULL, 
                            requirement TEXT)
                '''
        try:
            self.cursor.execute(sql)
            print("CREATE TABLE SUCCESS.")
        except Exception as ex:
            print(f"CREATE TABLE FAILED,CASE:{ex}")

    # 发送请求
    def get_data(self, page):
        data = {"channel": "group_official_site", "language": "zh", "batchId": "", "categories": "",
                "deptCodes": [], "key": "", "pageIndex": page, "pageSize": 10, "regions": "", "subCategories": ""}
        response = requests.post(self.url, headers=self.headers, json=data)
        return response.json()

    # 提取数据
    def parse_data(self, data):
        for i in data['content']['datas']:
            name = i['name']
            workLocations = ','.join(i['workLocations'])
            requirement = i['requirement']
            self.save_data(name, workLocations, requirement)

    # 保存数据
    def save_data(self, name, workLocations, requirement):
        # 存储sql 命令
        sql = 'INSERT INTO ali(id, workLocations, name, requirement) values(%s, %s, %s, %s)'
        try:
            self.cursor.execute(sql, (0, workLocations, name, requirement))
            # 提交
            self.db.commit()
            print('保存正常')
        except:
            print('保存失败')
            # 回调
            self.db.rollback()

    # 主函数
    def main(self):
        self.create_table()
        for i in range(1, 10):
            res = self.get_data(i)
            self.parse_data(res)


if __name__ == '__main__':
    ali = Ali()
    ali.main()
