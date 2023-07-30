




import re

# 匹配中文

data = '你好, hello, 世界'
print(re.findall('[\u4e00-\u9fa5]', data))

