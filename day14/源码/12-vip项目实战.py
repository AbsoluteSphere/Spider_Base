import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pymongo import MongoClient


class WeiPin():
    def __init__(self):
        self.client = MongoClient()
        self.col = self.client['spiders11']['vip']
        options = webdriver.ChromeOptions()
        options.add_experimental_option('useAutomationExtension', False)  # 去掉开发者警告
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 不加载图片
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        self.browser = webdriver.Chrome(options=options)
        self.browser.maximize_window()

    # 请求主页面
    def base(self):
        self.browser.get('https://www.vip.com/')
        wait = WebDriverWait(self.browser, 10)
        print(self.browser.page_source)
        inpu = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@class="c-search-input  J-search-input"]')))
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="c-search-button  J-search-button  J_fake_a"]')))
        inpu.send_keys('电脑')
        time.sleep(4)
        button.click()
        time.sleep(random.randint(1000, 1400)/ 1000)

    # 发送请求
    def get_data(self):
        pass

    # 提取数据
    def parse_data(self):
        pass

    # 保存数据
    def save_data(self):
        pass

    # 点击下一页
    def page_next(self):
        pass

    # 滚动页面
    def drop_down(self):
        pass

if __name__ == '__main__':
    vip = WeiPin()
    vip.base()
    vip.get_data()




