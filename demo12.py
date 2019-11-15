from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
browser = Chrome()
browser.get("https://www.momoshop.com.tw/main/Main.jsp/")
element1 = browser.find_element_by_id('keyword')
element1.clear()
element1.send_keys("洗衣粉")
element1.send_keys(Keys.RETURN)
time.sleep(10)
browser.close()