import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://36kr.com/')
for i in range(1, 10):
    time.sleep(1)
    browser.execute_script('window.scrollTo(0, {})'.format(i * 700))
