import asyncio
import aiomysql




async def test_mysql():
    conn = await aiomysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='spiders11')
    cur = await conn.cursor()
    await cur.execute('select * from ali')
    r = await cur.fetchall()
    print(r)

if __name__ == '__main__':
    # 创建事件循环
    loop = asyncio.get_event_loop()

    loop.run_until_complete(test_mysql())





