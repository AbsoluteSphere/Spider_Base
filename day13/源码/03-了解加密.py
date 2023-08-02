
import requests

url = 'https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
data = {"param":"WHtGXQexDBIuT8QhHCeEyK40PUljNQeVGC+wL1EWkaWM9c7xzFDwENX0Ex470PUyhDw628WuSEZYKJDxPiRZ7Hu1bBHIH1ti481Ixd3Zrq9X1Ke2l06nOndnDia7kRiYxZiTpPnkMyWlUUVyAeuFPpmt0X+NUKB5upllZzTWG1Yzk3aN5RVrzZz1ZydwvoyP4zqyqjS1zYxB7/kGe7XOqlCzqAyfbulGeOoq445BiCzsR8ZI72aBFMVusAHjSuLvkf1N3kH5xe2zVsqZCwisG9hal2ychGxsrkulkX4VRYrGaxZYG/p/RQi8m+d7c3lPUKB3aUq6G20V0mEjJQepijKdYVr8P1HGHef2g7EzsDZYqkT90mS1lko9b3BCTqHW9W9wJTRxSGaoKKzcGSCP/NeNHCCi8/ykJZwvDLeaKInD875VmKTqBiG+BGG97rbZasEEqk8ndOMn32bQgvN8BRzmWtgXygcw/nDUIf12yUGfcCxt1c2KOLqzee7yN/BUK02Dm2Vz96bjrCdHkGz7XsSKeAgBPjoCJitGvL6G3ibwuVXePR9XGr+anABPT+nXZ0XThDP4LMzRNLtwMmQNFp/EkMhdFP9561eewciiceFRzVoWCd34XpPRpwA++Q0M+UiJGvNgqwHNmHbF/C7LzoW4XnroLSzuLYjVb5nhc6E="}
response = requests.post(url, headers=headers, json=data)
print(response.text)