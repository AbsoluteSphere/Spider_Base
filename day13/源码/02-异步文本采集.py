import random

from lxml import etree
# 导入异步发送请求方式
import aiohttp
# 用来创建异步的方式
import asyncio.queues
# 异步数据库
import aiomysql


class Qiche():
    def __init__(self):
        # url就是输入的网址
        self.url = 'https://www.che168.com/china/a0_0msdgscncgpi1ltocsp{}exf4x0/?pvareaid=102179#currengpostion'
        self.headers = {
            'Cookie': 'fvlid=1687075785368AiGsuPNVlLaE; sessionid=da420410-0ac2-4463-b5be-67965b84b2ed; area=430104; che_sessionid=12E7357A-1F5A-4EFE-9BF8-FECFE04920C2%7C%7C2023-06-18+16%3A09%3A45.826%7C%7C0; carDownPrice=1; listuserarea=0; sessionip=175.0.58.200; sessionvisit=2c51aedf-2b95-4e2c-8629-2731de55a2af; sessionvisitInfo=da420410-0ac2-4463-b5be-67965b84b2ed||102179; Hm_lvt_d381ec2f88158113b9b76f14c497ed48=1687075786,1687097417,1687263097; che_sessionvid=9E993A59-2CCD-4200-888A-9815218C3CCF; UsedCarBrowseHistory=0%3A48286397%2C0%3A47987459%2C0%3A47991760%2C0%3A48294028; userarea=0; ahpvno=12; Hm_lpvt_d381ec2f88158113b9b76f14c497ed48=1687264912; ahuuid=F67AECF2-D0CD-46EC-B471-4E1E724E158A; showNum=30; v_no=32; visit_info_ad=12E7357A-1F5A-4EFE-9BF8-FECFE04920C2||9E993A59-2CCD-4200-888A-9815218C3CCF||-1||-1||32; che_ref=0%7C0%7C0%7C0%7C2023-06-20+20%3A41%3A52.964%7C2023-06-18+16%3A09%3A45.826; sessionuid=da420410-0ac2-4463-b5be-67965b84b2ed',
            'Referer': 'https://www.che168.com/china/a0_0msdgscncgpi1ltocsp3exf4x0/?pvareaid=102179',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        # json_url是获取详情的请求网址
        # 若返回值前面有configTitle(),把网址中的callback删掉就是JSON数据了
        self.json_url = 'https://cacheapigo.che168.com/CarProduct/GetParam.ashx?specid={}'

    async def info_get(self, id, client, pool):
        """
        获取详情数据
        :return:
        """
        response = await client.get(self.json_url.format(id))
        res_json = await response.json()
        if res_json['result'].get('paramtypeitems'):
            item = {}
            item['name'] = res_json['result']['paramtypeitems'][0]['paramitems'][0]['value']
            item['price'] = res_json['result']['paramtypeitems'][0]['paramitems'][1]['value']
            item['brand'] = res_json['result']['paramtypeitems'][0]['paramitems'][2]['value']
            item['length'] = res_json['result']['paramtypeitems'][1]['paramitems'][0]['value']
            item['breadth'] = res_json['result']['paramtypeitems'][1]['paramitems'][1]['value']
            item['altitude'] = res_json['result']['paramtypeitems'][1]['paramitems'][2]['value']

            await self.save_data(item, pool)

    async def get_data(self, page, client, pool):
        """
        获取主页面信息
        :return:
        """
        response = await client.get(self.url.format(page))
        # response.encoding = 'gbk'
        data = await response.text(encoding='gbk')
        html = etree.HTML(data)
        li_list = html.xpath('//ul[@class="viewlist_ul"]/li/@specid')
        # print(li_list)
        # print(len(li_list))
        tasks = []
        for id in li_list:
            res = self.info_get(id, client, pool)
            task = asyncio.create_task(res)
            tasks.append(task)
        await asyncio.wait(tasks)

    async def save_data(self, item, pool):

        async with pool.acquire() as conn:
            async with conn.cursor() as cursor:

                sql = 'INSERT INTO qiche(id, name, price, brand, altitude, breadth, length) values(%s, %s, %s, %s, %s, %s, %s)'
                try:
                    await cursor.execute(sql, (
                    0, item['name'], item['price'], item['brand'], item['altitude'], item['breadth'], item['length']))
                    await conn.commit()
                    print('插入成功')
                except Exception as e:
                    print('插入数据错误!!!', e)
                    # await con.rollback()

    async def main(self):
        # 创建数据库连接  通过连接池的方式创建连接
        pool = await aiomysql.create_pool(user='root', password='root', db='spiders11', loop=loop)
        # 用池子创建连接
        conn = await pool.acquire()
        cursor = await conn.cursor()
        # 先确定采集什么数据
        create_sql = '''
                    CREATE TABLE IF NOT EXISTS qiche(
                        id int primary key auto_increment not null,
                        name VARCHAR(255) NOT NULL,
                        price VARCHAR(255) NOT NULL,
                        brand VARCHAR(255) NOT NULL,
                        altitude VARCHAR(255) NOT NULL,
                        breadth VARCHAR(255) NOT NULL,
                        length VARCHAR(255) NOT NULL
                        );
                    '''
        await cursor.execute(create_sql)
        # 创建异步请求对象
        async with aiohttp.ClientSession(headers=self.headers) as client:
            print(client)
            tasks = []
            for i in range(1, 40):
                res = self.get_data(i, client, pool)
                task = asyncio.create_task(res)
                tasks.append(task)
                await asyncio.sleep(random.randint(500, 800) / 1000)
            await asyncio.wait(tasks)

        await cursor.close()
        conn.close()


if __name__ == '__main__':
    qc = Qiche()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(qc.main())
