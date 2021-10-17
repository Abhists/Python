from selenium import webdriver

import time

driver = webdriver.Firefox(r'C:\Users\admin\Desktop\Git projects\Python')
web_page = driver.get('https://www.youtube.com')
time.sleep(5)
driver.quit()