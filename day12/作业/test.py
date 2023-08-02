import aiohttp
import asyncio


class LOL:
    def __init__(self):
        self.url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2818252'
        self.skin_url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js?ts=2818268'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
    async def get_data(self, client, heroId, name):
        res = await client.get(self.skin_url.format(heroId), headers=self.headers)
        content = await res.json(content_type=None)
        print(content)
        # with open('LOL图片/' + name + '-' + '' + '.jpg', 'wb') as f:
        #     f.write(content)
    async def main(self):
        # async with 声明一个异步的上下文管理器,让程序自动分配和释放资源
        # aiohttp.ClientSession 和 requests.session() 类似
        async with aiohttp.ClientSession() as client:
            response = await client.get(self.url, headers=self.headers)
            lol_data = await response.json(content_type=None)
            task_list = []
            for i in lol_data['hero']:
                name = i['name']
                heroId = i['heroId']
                # res是一个协程对象
                res = self.get_data(client, heroId, name)
                # 转化为task对象
                task = asyncio.create_task(res)
                task_list.append(task)
            await asyncio.wait(task_list)
if __name__ == '__main__':
    lol = LOL()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(lol.main())
