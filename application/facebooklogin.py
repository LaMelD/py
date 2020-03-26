# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

id = ''
passwd = ''

driver = webdriver.Chrome('C:/Users/[유저]/AppData/Local/Programs/Python/chromedriver.exe')
driver.get("http://www.facebook.com")
elem = driver.find_element_by_name("email")
elem.send_keys(id)
elem = driver.find_element_by_name("pass")
elem.send_keys(passwd)
elem.send_keys(Keys.RETURN)