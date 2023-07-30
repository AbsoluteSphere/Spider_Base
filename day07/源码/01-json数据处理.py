

import json


dic1 = {'aa':'123234', 'bb':'柏汌'}
# 将字典数据转换成json数据
js_data = json.dumps(dic1, ensure_ascii=False, indent=4)
# 把json数据转换成字典
print(json.loads(js_data))

# 将python数据类型直接存 json文件  json.dump
with open('test.txt', 'w')as f:
    json.dump(dic1, f, ensure_ascii=False, indent=2)


# 将json文件数据  进行读取转换成字典数据json.load
with open('test.txt', 'r')as f:
    data = json.load(f)
    print(data)

