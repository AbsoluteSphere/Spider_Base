import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# 模拟键盘操作的库
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
#
# browser.get('https://www.baidu.com')
# # 选中一个元素     根据标签的name属性定位元素
# s = browser.find_element(By.NAME, 'wd')
# # 输入数据
# s.send_keys('python')
# s.send_keys(Keys.ENTER)
# time.sleep(3)
# # browser.quit()
# # 元素节点提取
#
# browser.find_element(By.ID)
# browser.find_element(By.CSS_SELECTOR)
# browser.find_element(By.XPATH)




# 获取多个元素标签

browser.get('https://www.icswb.com/channel-list-channel-161.html')
# 选取一个元素
# lis = browser.find_element(By.CSS_SELECTOR, '#NewsListContainer li')
# 获取多个元素
lis = browser.find_elements(By.CSS_SELECTOR, '#NewsListContainer li')
print(lis)

