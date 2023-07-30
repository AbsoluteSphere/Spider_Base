

# 导入re模块
import re

# #
# result = re.match('正则表达式的规则', 要匹配的字符串)
#
# # 获取到匹配的结果  通过group方法进行获取
# print(result.group())
# match 方法重头开始匹配
result = re.match('tuling', 'tuling.com')
# 获取结果
print(result.group())



