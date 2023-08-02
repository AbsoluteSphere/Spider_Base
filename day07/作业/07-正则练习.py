import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}
f = open('最新玄幻小说.txt', 'a+')
for i in range(1, 11):
    url = f'https://www.77xsw.cc/fenlei/1_{i}/'
    result = requests.get(url, headers=headers)
    result.encoding = "gbk"
    print(result.text)
    details = re.findall('<span class="sp_2"><a href="(.*?)" target="_blank" title="(.*?)">', result.text)
    for href, title in details:
        print(href, title)
        f.write(f"{title}:{href}\n")
f.close()