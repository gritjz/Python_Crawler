from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

bro = webdriver.Chrome(executable_path='./chromedriver')

bro.get('https://qzone.qq.com/')

bro.switch_to.frame('login_frame')

a_tag = bro.find_element_by_id('switcher_plogin')
a_tag.click()

userName_tag = bro.find_element_by_id('u')
password_tag = bro.find_element_by_id('p')

userName_tag.send_keys('446928479')
password_tag.send_keys('Zhang811')

btn= bro.find_element_by_id('login_button')
btn.click()

sleep(3)

#bro.quit()