import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchFrameException

# 设置屏蔽
options = webdriver.ChromeOptions()
# 屏蔽检测
options.add_argument('--disable-blink-features=AutomationControlled')

browser = webdriver.Chrome(options=options)

browser.get('https://bot.sannysoft.com/')
time.sleep(5)