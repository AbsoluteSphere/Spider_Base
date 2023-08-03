"""
地址：https://search.suning.com/%E7%94%B5%E8%84%91/
技术：selenium自动化
字段：价格、标题   可以自行拓展
保存：mongo
交付： 数据入库截图
"""

import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymongo


class SuNing:
    def __init__(self):
        self.url = 'https://search.suning.com/%E7%94%B5%E8%84%91/'
        # 给浏览器加载配置
        options = webdriver.ChromeOptions()
        # 屏蔽检测
        options.add_argument('--disable-blink-features=AutomationControlled')
        # 禁止图片
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        # 无头模式   不会打开浏览器页面     也会节省时间   确保代码没有问题 就能使用
        # options.add_argument('-headless')
        # 隐藏"Chrome正在受到自动软件的控制"
        options.add_experimental_option('useAutomationExtension', False)  # 去掉开发者警告
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.browser = webdriver.Chrome(options=options)
        # 浏览器最大化
        self.browser.maximize_window()
        self.client = pymongo.MongoClient()
        self.collection = self.client['spider_mongo']['suning']

    def base(self):
        self.browser.get(self.url)
        wait = WebDriverWait(self.browser, 10)
        # 判断元素是否加载在页面上
        input = wait.until(EC.presence_of_element_located((By.ID, 'searchKeywords')))
        button = wait.until(EC.element_to_be_clickable((By.ID, 'searchSubmit')))
        input.send_keys('笔记本')
        time.sleep(1)
        # 判断当前元素是否能点击
        button.click()
        time.sleep(random.randint(1000, 1400) / 1000)

    def parse_data(self):
        self.drop_down()
        res_info = self.browser.find_elements(By.XPATH, "//div[@class='res-info']")
        for i in res_info:
            item = {}
            item['title'] = i.find_element(By.XPATH, './div[@class="title-selling-point"]').text
            item['price'] = i.find_element(By.XPATH, './div[@class="price-box"]').text
            self.save_data(item)
        self.next_page()

    def save_data(self, item):
        self.collection.insert_one(item)
        print('插入成功！')

    def next_page(self):
        try:
            next_page = self.browser.find_element(By.XPATH, '//a[@id="nextPage"]')
            if next_page:
                next_page.click()
                self.parse_data()
            else:
                self.browser.quit()
                return
        except Exception as e:
            print('没有下一页！')
            self.browser.quit()
            return

    def drop_down(self):
        for i in range(1, 11):
            js = f'document.documentElement.scrollTop={i * 1500}'
            self.browser.execute_script(js)
            time.sleep(random.randint(500, 800) / 1000)
        # 到底后，回滚一段距离，使“下一页”可见
        self.browser.execute_script("window.scrollBy(0, -600)")
        time.sleep(1)

    def main(self):
        self.base()
        self.parse_data()


if __name__ == '__main__':
    suning = SuNing()
    suning.main()
