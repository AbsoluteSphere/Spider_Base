
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')

# alt + enter 可以快速导包

# 输入数据
browser.find_element('xpath', 'kw').send_keys()
# 情况输入框
browser.find_element(By.ID, 'kw').clear()
# 点击
browser.find_element(By.ID, 'kw').click()





