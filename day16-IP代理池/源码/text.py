import pyhttpx

s = pyhttpx.HttpSession()
headers = {
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    # "Accept-Language": "zh-CN,zh;q=0.9",
    # "Cache-Control": "no-cache",
    # "Connection": "keep-alive",
    # "Pragma": "no-cache",
    # "Sec-Fetch-Dest": "document",
    # "Sec-Fetch-Mode": "navigate",
    # "Sec-Fetch-Site": "none",
    # "Sec-Fetch-User": "?1",
    # "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "downlink": "8.15",
    "ect": "4g",
    "rtt": "50",
    # "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    # "sec-ch-ua-mobile": "?0",
    # "sec-ch-ua-platform": "\"Windows\"",
    # "sec-ch-ua-platform-version": "\"8.0.0\"",
    # "cookie": 'session-id=457-9487922-6391357; session-id-time=2082787201l; i18n-prefs=CNY; ubid-acbcn=460-5730979-9030509; session-token="kXLPW0gfnbMZoBpSu0JLNpPaWYIDSULWLTK6F3EDP77FUnbAmibjNAGwUfJv4116fMLTfVb2owCOBlo36mRMNCbE8wEH79y90MD9njul8JKlOsHGQaVFeZt1Iq1sOJOhwgidHg9hue0sC2W0DdlsZbZQR7T9nEySvIfRYY6sO1KzKbnLi1LM6PBTdnNkOa4k3WG6MuvYVvtp+tPCbQvYuV22yZgWjCImH4aIiS1Vxf8="; csm-hit=tb:TMEDHZ2KGA8NKGYM0EA5+s-042RMD9W6Y1HAV3K3KXR|1688050119869&t:1688050119869&adb:adblk_yes'
}
url = "https://www.amazon.cn/s"
params = {
    "bbn": "2016156051",
    "rh": "n:2153993051",
    "fs": "true",
    "ref": "lp_2153993051_sar"
}
response = s.get(url, headers=headers, params=params)
print(response.content.decode())
print(response)
