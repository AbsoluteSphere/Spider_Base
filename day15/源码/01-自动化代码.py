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
        # print(self.browser.page_source)
        inpu = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@class="c-search-input  J-search-input"]')))
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="c-search-button  J-search-button  J_fake_a"]')))
        inpu.send_keys('电脑')
        time.sleep(4)
        button.click()
        time.sleep(random.randint(1000, 1400)/ 1000)


    # 提取数据
    def parse_data(self):
        self.drop_down()
        # print(self.browser.page_source)
        node_list = self.browser.find_elements(By.XPATH, '//section[@id="J_searchCatList"]/div[@class="c-goods-item  J-goods-item c-goods-item--auto-width"]')
        # print(node_list)
        for node in node_list:
            # 获取的数据  是webdirve数据类型
            price = node.find_element(By.XPATH, './/div[@class="c-goods-item__sale-price J-goods-item__sale-price"]').text
            title = node.find_element(By.XPATH, './a/div[2]/div[2]').text
            try:
                discount = node.find_element(By.XPATH,
                                             './/div[@class="c-goods-item__main-price     J-goods-item__main-price"]/div[@class="c-goods-item__discount  J-goods-item__discount"]').text
            except Exception as e:
                print('数据为空')
                discount = '空'
            try:
                market_price = node.find_element(By.XPATH,
                                                 './/div[@class="c-goods-item__market-price  J-goods-item__market-price"]').text
            except Exception as e:
                print('数据为空')
                market_price = '空'

            item = {
                'title': title,
                'price': price,
                'discount': discount,
                'market_price': market_price
            }
            print(item)
            self.save_data(item)
        self.page_next()
    # 保存数据
    def save_data(self, item):
        self.col.insert_one(item)

    # 点击下一页
    def page_next(self):
        try:
            button = self.browser.find_element(By.XPATH, '//*[@id="J_nextPage_link"]')
            if button:
                button.click()
                self.parse_data()
            else:
                self.browser.quit()

        except Exception as e:
            print('下一頁沒有定位到！！！')
            self.browser.quit()


    # 滚动页面
    def drop_down(self):
        for x in range(1, 10):
            js = 'document.documentElement.scrollTop = {}'.format(x * 1000)
            self.browser.execute_script(js)
            time.sleep(random.randint(500, 800) / 1000)



if __name__ == '__main__':
    vip = WeiPin()
    vip.base()
    vip.parse_data()




