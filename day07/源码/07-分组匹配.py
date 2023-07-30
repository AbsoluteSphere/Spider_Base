


import re


# | 匹配左右两边的任意一个表达式
# 需求：在列表中["apple", "banana", "orange", "pear"]，匹配apple和pear
# data =  ["apple", "banana", "orange", "pear"]
# for i in data:
#     res = re.match('apple|pear', i)
#     # print(res)
#     if res:
#         print(res.group())
#     else:
#         print('{}不喜欢'.format(i))


# ()
# 匹配出163、126、qq等邮箱
# res = re.match('\w{4,20}@(163|126|qq)(\.com)', 'hellowww@163.com')
# print(res)
# print(res.group(3))

# \num  引用分组匹配到的字符串
# data = '<html>hh</html>'
# res = re.match('<([a-zA-Z1-6]+)>hh</\\1>', data)
# print(res.group())


# (?P) 给分组起名字    (?P=name)  引用名字
data = '<html><h1>www.tuling.cn</h1></html>'
res = re.match('<(?P<name1>[a-zA-Z1-6]+)><(?P<name2>[a-zA-Z1-6]+)>www.tuling.cn</(?P=name2)></(?P=name1)>', data)
print(res.group())