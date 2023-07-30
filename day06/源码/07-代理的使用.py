

# 网址
import requests

url = 'http://httpbin.org/ip'
proxies = {
    'http': "http://106.15.190.190:3128",
    # 'https': "https://106.15.190.190:3128",
}
response = requests.get(url, proxies=proxies)
print(response.text)


