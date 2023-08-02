import time

from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser = webdriver.Edge()
# webdriver.
# post
browser.get('https://ww.baidu.com')

# 方法弃用    selenium3    selenium4
# browser.find_element_by_xpath('kw').send_keys('柏汌真帅')

# 定位到输入框  输入数据
browser.find_element(By.ID, 'kw').send_keys('柏汌真帅')

# 定位到按钮  进行点击
browser.find_element(By.XPATH, '//*[@id="su"]').click()
time.sleep(3)
# 提取页面数据  获取的数据渲染之后的页面数据
print(browser.page_source.encode('utf-8'))
# 提取cookie
print(browser.get_cookies())
# 获取当前页面的截屏
browser.get_screenshot_as_file('123.png')
# 获取到当前的请求地址
print(browser.current_url)



time.sleep(3)

# 关闭浏览器
browser.quit()