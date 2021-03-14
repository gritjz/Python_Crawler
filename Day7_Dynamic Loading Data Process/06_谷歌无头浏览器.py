from selenium import webdriver
from time import sleep
#用来实现无可视化界面
from selenium.webdriver.chrome.options import Options
#实现规避检测
from selenium.webdriver import ChromeOptions

#实现无可视化的操作
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('disable-gpu')

#如何实现 让selenium规避被检测到的风险
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])


bro = webdriver.Chrome(executable_path='./chromedriver',
                       chrome_options=chrome_options,
                       options=option)

#无可视化界面, phantomJs
bro.get('https://www.baidu.com/')

print(bro.page_source)
sleep(2)
bro.quit()
