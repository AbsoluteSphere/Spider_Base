
import pymongo

client = pymongo.MongoClient()

# 创建的集合
collection = client['stu']['abc']

# 插入单条数据
data = {'id': '001', 'name': '柏汌', 'age': '18'}
res = collection.insert_one(data)
print(res)


data1 = {'id': '002', 'name': '双双', 'age': '18'}
data2 = {'id': '003', 'name': '安娜', 'age': '18'}
collection.insert_many([data1, data2])
