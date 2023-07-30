

import requests
import csv

with open('bzhan.csv', 'a', encoding='utf-8', newline='')as f:
    fi_name = ['author', 'arcurl', 'duration', 'description', 'play', 'danmaku']
    csv_f = csv.DictWriter(f, fieldnames=fi_name)
    # 写入表头
    csv_f.writeheader()
    # 获取资源地址
    for i in range(1, 10):
        url = 'https://api.bilibili.com/x/web-interface/wbi/search/type?__refresh__=true&_extra=&context=&page={}&page_size=42&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=%E7%BE%8E%E5%A5%B3&qv_id=em8RYFzu8hBolRvv0LFMyTmBiEj49br8&ad_resource=5654&source_tag=3&gaia_vtoken=&category_id=&search_type=video&dynamic_offset=216&web_location=1430654&w_rid=b46daa127fe20e780f6d3949dff844ce&wts=1686488047'

        headers = {
            'Cookie':"buvid3=2CBA399F-32D0-896C-0FD4-2F4AE19EB98877738infoc; b_nut=1683793377; _uuid=5CB2AAA10-26BE-3910E-3182-26289105EC10D680550infoc; buvid_fp=1486b7a3fb0aab3d19a04098238c4a85; buvid4=DD72BE04-93B6-DF5C-38E2-74958855F85A81463-023051116-PHT9I2IYys7HmatUTSWh9Q%3D%3D; CURRENT_FNVAL=4048; rpdid=|(kmJY|kYl)l0J'uY)J)uJ)kk; DedeUserID=1892223867; DedeUserID__ckMd5=4e3cb95f66216458; i-wanna-go-back=-1; b_ut=5; header_theme_version=CLOSE; home_feed_column=5; browser_resolution=1920-929; nostalgia_conf=-1; CURRENT_QUALITY=80; PVID=1; bp_video_offset_1892223867=803276137220276200; FEED_LIVE_VERSION=V_LIVE_2; SESSDATA=cce86ff9%2C1701864039%2C866b8%2A62; bili_jct=ebef78242abeaf289b4dfb31db16ea4a; b_lsid=7BBE21014_188AA82E563; sid=6crkuc6r",
            # 'Origin':'https://search.bilibili.com',
            # 'Referer':'https://www.bilibili.com/',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        # 发送请求  反爬
        response = requests.get(url.format(i), headers=headers)

        # 提取数据   提取数据的方法
        data = response.json()['data']['result']

        for i in data:
            item = {}
            item['author'] = i['author']
            item['arcurl'] = i['arcurl']
            item['duration'] = i['duration']
            item['description'] = i['description']
            item['play'] = i['play']
            item['danmaku'] = i['danmaku']
            csv_f.writerow(item)