

import re

# ^ 匹配特定的字符开头
# res = re.match('^\d.*', 'lsdhjfkjlsd')
# print(res.group())

# $ 以特定的字符结尾
# res = re.match('.*\d$', 'sdjfhjksdfh7')
# print(res.group())


# ^ 特殊用法  放在中括号里面   除了中括号里面的值  其他的都能匹配
res = re.match('[^12345].*', '6sdfhjk')
print(res.group())
