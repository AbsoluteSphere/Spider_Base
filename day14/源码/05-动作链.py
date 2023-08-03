
from selenium import webdriver
# 执行动作链的模块
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
log = browser.find_element(By.XPATH, '//div[@id="iframewrapper"]/iframe')
browser.switch_to.frame(log)

min = browser.find_element(By.ID, 'draggable')
max = browser.find_element(By.ID, 'droppable')
# 创建一个动作链
action = ActionChains(browser)
# 拖动元素
action.drag_and_drop(min, max)
# 执行命令
action.perform()