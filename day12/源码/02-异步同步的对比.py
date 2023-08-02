# import time
# import requests
# def main():
#     for i in range(30):
#         res = requests.get('https://www.baidu.com')
#         print(f'第{i + 1}次请求，status_code = {res.status_code}')
#
# if __name__ == '__main__':
#     start = time.time()
#     main()
#     end = time.time()
#     print(f'同步发送30次请求，耗时：{end - start}')


import asyncio
import time

import aiohttp  # pip install aiohttp

async def get_Data(client, i):
    res = await client.get('https://www.baidu.com')
    print(f'第{i + 1}次请求，status_code = {res.status}')
    return res


async def main():
    # async with 声明一个异步的上下文管理器,让程序自动分配和释放资源
    # aiohttp.ClientSession 和 requests.session() 类似
    # 创建连接对象client
    async with aiohttp.ClientSession() as client:
        task_list = []
        for i in range(30):
            # 调用异步函数  会返回协程对象
            res = get_Data(client, i)
            # print(res)
            # 协程对象转换成task对象
            task = asyncio.create_task(res)
            task_list.append(task)
            # await get_Data(client, i)
        # task任务批量提交 done是结果 pending是状态
        # wait可以接收一个迭代对象并将迭代对象中的元素提交给事件循环 并且可以获取被提交的任务的运行状态
        done, pending = await asyncio.wait(task_list)
        # print(done, pending)
        # for i in done:
        #     print(i.result())


if __name__ == '__main__':
    t1 = time.time()

    # 开始事件循环对象
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(f'同步发送30次请求，耗时：{time.time() - t1}')
