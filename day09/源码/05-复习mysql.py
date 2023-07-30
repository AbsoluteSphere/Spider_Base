
import pymysql


# 连接数据库
db = pymysql.connect(host='localhost', user='root', password='root', db='spiders11')
# 创建一个游标对象
cursor = db.cursor()

# cursor.execute('select version()')
# data = cursor.fetchone()
# print(data)
# 创建数据库
# cursor.execute('CREATE DATABASE spiders11 DEFAULT CHARACTER SET utf8')
# 准备好创建表的命令
sql = '''
CREATE TABLE IF NOT EXISTS students (
        id VARCHAR(255) NOT NULL, 
        name VARCHAR(255) NOT NULL, 
        age INT NOT NULL, 
        PRIMARY KEY (id))

'''
try:
    cursor.execute(sql)
    print('创建成功')
except:
    print('创建失败')
finally:



    # 关闭数据库连接
    db.close()





