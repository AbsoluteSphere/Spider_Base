import requests
import pymongo


def get_data(page):
    url = 'https://api.douguo.net/home/notes/{}/20'.format(20*page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; SM-G988N Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36'
    }
    data = {
        'client': '4',
        '_session': '16878742555533404350631bc7b31',
        'direction': '2',
        'btmid': {},
        'is_new_user': '0',
        'request_count': '10',
        'sign_ran': 'cff2507274e1ced87612c572ed6925c8',
        'code': 'a2b996f999ae6ac2',
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()


def parse_data(response):
    for node in response['result']['list']:
        item = {}
        item['title'] = node['note']['title']
        item['img_url'] = node['note']['image_u']
        item['author'] = node['note']['author']['n']
        print(item)
        save_data(item)


def save_data(item):
    col.insert_one(item)


def main():
    for i in range(1, 5):
        # https://api.douguo.net/home/notes/60/20
        # https://api.douguo.net/home/notes/40/20
        response = get_data(i)
        parse_data(response)


if __name__ == '__main__':
    client = pymongo.MongoClient()
    col = client['spiders11']['douguo']
    main()
