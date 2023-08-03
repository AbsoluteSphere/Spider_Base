import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pymongo import MongoClient


class SuNing:
    def __init__(self):
        self.url = 'https://search.suning.com/%E7%94%B5%E8%84%91/'
        self.browser = webdriver.Chrome(chrome_init.init(img=True))
        self.wait = WebDriverWait(self.browser, 10)
        self.client = MongoClient(host='localhost', port=27017)
        self.collection = self.client['pymongo']['SuNing']

    def get_url(self):
        '''
        获取主页
        :return:
        '''
        self.browser.get(self.url)
        self.browser.maximize_window()
        input = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="searchKeywords"]')))
        button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="searchSubmit"]')))
        time.sleep(random.randint(500, 800) / 1000)
        input.clear()
        input.send_keys('笔记本电脑')
        time.sleep(random.randint(500, 800) / 1000)
        button.click()

    def parse_data(self):
        '''
        处理数据
        :return:
        '''
        # 下滑
        self.drop_down()
        li_list = self.browser.find_elements(By.XPATH, '//div[@class="res-info"]')
        for li in li_list:
            item = {
                'title': li.find_element(By.XPATH, './div[@class="title-selling-point"]/a').text,
                'price': li.find_element(By.XPATH, './div[@class="price-box"]/span').text
            }
            print(item)
            # 保存数据
            self.save_data(item)
        # 下一页
        self.next_page()

    def save_data(self, item):
        '''
        保存数据
        :return:
        '''

        self.collection.insert_one(item)
        print("插入成功：", item)

    def next_page(self):
        '''
        翻页
        :return:
        '''
        try:
            next_page = self.browser.find_element(By.XPATH, '//a[@id="nextPage"]')
            # 有可能仍存在，但不可见
            if next_page:
                # 点击下一页，重新处理数据
                next_page.click()
                self.parse_data()
            else:
                print("下一页没了")
                self.browser.quit()
                return
        except Exception as e:
            print("下一页没了")
            self.browser.quit()
            return

    def drop_down(self):
        '''
        下滑
        :return:
        '''
        for x in range(1, 10):
            # 上滑
            js = f"document.documentElement.scrollTop = {x * 2000}"
            self.browser.execute_script(js)
            time.sleep(random.randint(500, 800) / 1000)
        # 到底后，回滚一段距离，使“下一页”可见
        self.browser.execute_script("window.scrollBy(0, -700)")

    def run(self):
        self.get_url()
        self.parse_data()


if __name__ == '__main__':
    sn = SuNing()
    sn.run()