import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.baidu.com')
time.sleep(3)
browser.switch_to.window(browser.window_handles[0])
time.sleep(2)
browser.get('https://pic.netbian.com/4kmeinv/index.html')
time.sleep(2)