
import re


# *匹配0次或者无限次
# result = re.match('12122[a-z]*', 'aaaaaaaa')
# print(result.group())

# + 匹配前面的字符出现1次或者无限次
# result = re.match('[a-z]+', 'aaaaaaaa')
# print(result.group())

# 匹配一个字符串，第一个字符是t,最后一个字符串是o,中间至少有一个字符
# result = re.match('t.+o', 'to')
# print(result.group())

# ?  前面的字符出现0次或者1次
# 匹配出这样的数据，但是https 这个s可能有，也可能是http 这个s没有
# res = re.match('https?', 'httpss')
# print(res.group())

# {m}  匹配括号里面出现的次数
# result = re.match('\d{6}', '1234567')
# print(result.group())

# {m,n} 匹配前面的字符出现 m-n次
result = re.match('\w{8,20}', 'ksdjhfjsdasdfksdhk')
print(result.group())

