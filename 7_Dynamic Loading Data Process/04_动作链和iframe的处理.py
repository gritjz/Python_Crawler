from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

bro = webdriver.Chrome(executable_path='./chromedriver')

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

#如果定位的标签是存在于iframe中，则必须通过如下操作进行标签定位

#切换浏览器标签定位的作用域
bro.switch_to.frame('iframeResult')
div = bro.find_element_by_id('draggable')

#动作链
action = ActionChains(bro)
#点击长按
action.click_and_hold(div)

for i in range(5):
    #perform()执行动作链
    action.move_by_offset(17, 0).perform()
    sleep(0.3)
#释放动作链
action.release()

bro.quit()