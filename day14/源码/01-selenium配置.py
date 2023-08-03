import time

from selenium import webdriver

# 给浏览器加载配置
options = webdriver.ChromeOptions()

# 禁止图片
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)

# 无头模式   不会打开浏览器页面     也会节省时间   确保代码没有问题 就能使用
# options.add_argument('-headless')

user_agent = 'ashdfjksdhjkfhsdjkfhjksd'
options.add_argument('user-agent={}'.format(user_agent))

#隐藏"Chrome正在受到自动软件的控制"
options.add_experimental_option('useAutomationExtension', False) # 去掉开发者警告
options.add_experimental_option('excludeSwitches', ['enable-automation'])

# 添加代理   ip被封的时候    网站有风控     需要验证码
# options.add_argument('--proxy-server=http://127.0.0.1:7890')


browser = webdriver.Chrome(options=options)
browser.get('http://www.baidu.com')
# 浏览器最大化
browser.maximize_window()
browser.set_window_size(800, 800)

# 执行js代码
browser.execute_script('window.open("https://www.baidu.com")')

time.sleep(15)
browser.quit()

