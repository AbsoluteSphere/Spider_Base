


# 貂蝉
# https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/141/141-bigskin-9.jpg
# https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/141/141-bigskin-8.jpg
# https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/141/141-bigskin-6.jpg
# https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/141/141-bigskin-6.jpg
# https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/141/141-bigskin-5.jpg
# https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/141/141-bigskin-4.jpg
# https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/141/141-bigskin-1.jpg

# 摇
# https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/505/505-bigskin-4.jpg
# https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/523/523-bigskin-4.jpg

# 是所有英雄编号的地址
# https://pvp.qq.com/web201605/js/herolist.json
import aiohttp
import asyncio

class wZRY():
    def __init__(self):
        self.url = 'https://pvp.qq.com/web201605/js/herolist.json'
        self.skin_url = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }

    async def get_Data(self, client, ename, cname):
        for i in range(1, 30):
            print(self.skin_url.format(ename, ename, i))
            res = await client.get(self.skin_url.format(ename, ename, i), headers=self.headers)
            if res.status == 200:
                content = await res.read()
                with open('wzry/' + cname + '-' + str(i) + '.jpg', 'wb')as f:
                    f.write(content)
                    print('正在下载{}第{}张图片'.format(cname, i))

            else:
                break



    async def run(self):
        async with aiohttp.ClientSession() as client:
            response = await client.get(self.url, headers=self.headers)
            wz_data = await response.json(content_type=None)
            # print()
            task_list = []
            for i in wz_data:
                ename = i['ename']
                cname = i['cname']
                res = self.get_Data(client, ename, cname)
                task = asyncio.create_task(res)
                task_list.append(task)
            await asyncio.wait(task_list)


if __name__ == '__main__':
    wzry = wZRY()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(wzry.run())

