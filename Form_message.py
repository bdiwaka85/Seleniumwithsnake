'''
Created on Apr 3, 2020

code to enter a message in a text box inside a form

@author: Diwakar
'''
#import the webdriver
from selenium import webdriver
import time

browser = webdriver.Chrome("D:\webdrivers\chromedriver.exe")
browser.maximize_window()
browser.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
time.sleep(3)
#identify the drop down using XPATH
browser.find_element_by_xpath("//form//input[@id='user-message']").send_keys("what's in a message")
browser.find_element_by_xpath("//button[contains(text(), 'Show Message')]").click()

time.sleep(2)
#close browser
browser.close()

