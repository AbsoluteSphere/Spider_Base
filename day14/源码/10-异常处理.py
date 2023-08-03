from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchFrameException

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except Exception as e:
    print('time out')

