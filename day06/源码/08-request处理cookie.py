import requests

url = 'http://www.cninfo.com.cn/new/disclosure'
# 1,在请求头里带上cookie字段
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    # 'Cookie': 'JSESSIONID=42C2FBDDF2331E75A0101C12B8297F29; insert_cookie=37836164; routeId=.uc1; _sp_ses.2141=*; _sp_id.2141=d148dc5e-1367-41f0-8687-a1660aecb743.1684409588.4.1685885631.1685883137.52193a80-088d-4b9c-8958-84d7524b98d7'
}
data = {
    'column': 'szse_latest',
    'pageNum': '2',
    'pageSize': '30',
    'sortName': '',
    'sortType': '',
    'clusterFlag': 'true',
}
# response = requests.post(url, headers=headers, data=data)
# print(response.request.headers)
# print(response.json())

# 2.单独携带cookie参数
cookies = {
    'JSESSIONID': '42C2FBDDF2331E75A0101C12B8297F29',
    'insert_cookie': '37836164',
    'routeId': '.uc1',
    '_sp_ses.2141': '*',
    '_sp_id.2141': 'd148dc5e-1367-41f0-8687-a1660aecb743.1684409588.4.1685885631.1685883137.52193a80-088d-4b9c-8958-84d7524b98d7',
}
res = requests.post(url, headers=headers, data=data, cookies=cookies)
print(res.request.headers)
print(res.json())