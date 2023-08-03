import time

from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('https://www.douban.com/')

log_iframe = browser.find_element(By.XPATH, '//div[@class="login"]/iframe')
browser.switch_to.frame(log_iframe)
browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/ul[1]/li[2]').click()
browser.find_element(By.NAME, 'username').send_keys('10086')
# browser.find_element('xpath', '/html/body/div[1]/div[1]/ul[1]/li[2]').click()
time.sleep(5)

# xpath 下标是从1开始的
