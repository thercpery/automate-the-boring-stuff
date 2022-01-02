#! python3

import pyinputplus as pyip
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username = pyip.inputStr("Enter your email:\n")
password = pyip.inputPassword("Enter your password:\n")
msg = pyip.inputStr("Enter your message:\n")
browser = webdriver.Chrome()
browser.get("https://www.messenger.com/")
time.sleep(5)
usernameElement = browser.find_element_by_id("email")
passElement = browser.find_element_by_id("pass")
usernameElement.send_keys(username)
passElement.send_keys(password)
passElement.submit()
time.sleep(20)
messageElement = browser.find_element_by_id("jsc_c_y")
messageElement.send_keys(msg)
messageElement.send_keys(Keys.ENTER)
time.sleep(10)

