
# 请求重试
import requests
from retrying import retry


# stop_max_attempt_number设置重试次数  重试3次
@retry(stop_max_attempt_number=3)
def get_data(url):
    print('1111')
    response = requests.get(url, timeout=0.1)
    # print(response.text)

    assert response.status_code == 200, '状态码响应不对'
    return response

get_data('https://yjcclm.com/')



