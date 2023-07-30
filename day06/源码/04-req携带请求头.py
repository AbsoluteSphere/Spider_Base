import requests

url = 'https://www.baidu.com/'
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=head)
# requests默认带的请求头
print(response.request.headers)
print(response.text)