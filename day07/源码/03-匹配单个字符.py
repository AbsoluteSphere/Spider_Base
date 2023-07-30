
import re

# . 匹配任意一个字符
# result = re.match('.', '1好')
# print(result.group())
#
# result = re.match('t.o', 'txo')
# print(result.group())

# [] 匹配括号中列举的数据
# res = re.match('[hHasdf]ello', 'xello')
# print(res.group())

# 匹配数字 \d 匹配从0-9
# result = re.match('[0-9][0-9]hello', '10hello')
# print(result.group())
# result = re.match('\dhello', '6hello')
# print(result.group())

# \D 匹配非数字
# result = re.match('\Dhello', '\nhello')
# print(result.group())


# \s 匹配空格
# res = re.match('hello\sworld', 'hello\rworld')
# print(res.group())

# \S 匹配非空格
# res = re.match('hello\Sworld', 'hello好world')
# print(res.group())

# \w 匹配非特殊字符
# res = re.match('hello\wworld', 'helloaworld')
# print(res.group())

# \W  匹配特殊字符
# res = re.match('hello\Wworld', 'hello%world')
# print(res.group())
