import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}
for i in range(1641, 1647):
    url = f'https://downsc.chinaz.net/Files/DownLoad/sound1/202303/y{i}.mp3'
    result = requests.get(url, headers=headers)
    # print(result)
    with open(f'./音频/{i}.mp3', 'wb') as f:
        f.write(result.content)