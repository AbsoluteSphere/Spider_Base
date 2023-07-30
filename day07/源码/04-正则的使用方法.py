
import re
# res = re.match('rrr', 'rrrr')
# print(res.group())

# search  重中间开始找  找一个数据
# res = re.search('abc', 'aaaabc')
# print(res.group())

# findall  找所有匹配规则的数据  获取的数据是列表  没有数据  是空列表
# res = re.findall('\d', '123aa456a5678a789b980c')
# print(res)

# sub 替换     传递3个参数
# re.sub('替换的规则', '替换的内容', '替换的文本数据')
# res = re.sub('\d', '_', 'ytu345ling34')
# print(res)

# compile 编译

# p = re.compile('\d')
#
# print(p.findall('sdkjhfjks4235453'))

print(re.sub('.', '_', 'asfsdfssdgdf\ngdfghdfgdfgdf', count=2))

# res = re.findall('.*', '123aa456a5678a789b980c324345dfghdfh4536564756786782\n34345456', re.S)
# print(res)