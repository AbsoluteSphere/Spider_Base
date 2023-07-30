
import requests
from bs4 import BeautifulSoup



# 获取到资源地址

url = 'https://sc.chinaz.com/yinxiao/index_7.html'
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')
div_list = soup.select('#AudioList .container .audio-item')
for div in div_list:
    title = div.select('.name')[0].getText().strip()
    mp3_url = div.select('audio')[0].get('src') if 'http' in div.select('audio')[0].get('src') else 'https:' + div.select('audio')[0].get('src')
    print(title, mp3_url)
    with open('铃声/' + title + '.mp3', 'wb')as f:
        res = requests.get(mp3_url, headers=headers)
        f.write(res.content)


