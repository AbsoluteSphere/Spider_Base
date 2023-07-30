

import pymysql


db = pymysql.connect(host='127.0.0.1', user='root', password='root', db='spiders11')
cursor = db.cursor()
# 插入语句
sql = 'insert into students(id, name, age) values(%s, %s, %s)'
try:
    print('插入成功')
    cursor.execute(sql, ('001', '柏汌', 18))
    # 提交到数据库
    db.commit()
except:
    print('数据出错')
    db.rollback()
finally:
    db.close()
