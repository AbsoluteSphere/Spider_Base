
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://pic.netbian.com/4kmeinv/index.html')
img_list = browser.find_elements(By.XPATH, '//ul[@class="clearfix"]/li/a/b')
for i in  img_list:
    print(i.get_attribute(''))


