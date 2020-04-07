'''
Created on Apr 3, 2020

code to get all the options in a dropdown list in a website

@author: Diwakar
'''
#import the webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import Select
#import time

browser = webdriver.Chrome("D:\webdrivers\chromedriver.exe")

browser.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")

#select the dropdown and print all values
#identify the drop down using XPATH
drop_down = Select(browser.find_element_by_xpath("//select[@id='select-demo']"))
#get the options tag *** note the elements and not element
drop_down_opt = [each for each in  drop_down.options]

for each in drop_down_opt[1:]:
    print(each.get_attribute("value"))
    
#close browser
browser.close()

