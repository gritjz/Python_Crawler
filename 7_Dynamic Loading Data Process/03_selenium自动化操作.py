from selenium import webdriver
from time import sleep
bro = webdriver.Chrome(executable_path='./chromedriver')

bro.get('https://world.taobao.com/')

#定位搜索栏
search_input = bro.find_element_by_id('mq')
#输入搜索信息
search_input.send_keys('iPhone 12')

#执行js程序，滚屏到底
bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')
sleep(2)

#定位搜索按钮
button = bro.find_element_by_xpath('//*[@id="J_PopSearch"]/div[1]/div/form/input[2]')
#点击搜索
button.click()


bro.get('https://www.baidu.com')
sleep(2)
#网页后退和前进
bro.back()
bro.forward()


sleep(5)
bro.quit()