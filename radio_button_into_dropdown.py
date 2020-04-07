'''
Created on Apr 3, 2020

code to get all the options in a dropdown list in a website

@author: Balaji
'''
#import the webdriver
from selenium import webdriver

browser = webdriver.Chrome("D:\webdrivers\chromedriver.exe")
browser.minimize_window()

browser.get("file:///C:/Users/Diwakar/Desktop/HomeDel.html")

#this is to wait till the page loads implicit
browser.implicitly_wait

def dropdown_func(xpath):
    drop_down_dd = browser.find_elements_by_xpath(xpath)
    for options in drop_down_dd:
        values = options.text.split('\n')
    return values

#locate the radio button for Vegetarian and click
veg = browser.find_element_by_xpath("//input[@name='foodType' and @value='veg']")
veg.click()

# retrieve maindish & Curry values
veg_main_dish = dropdown_func("//select[@id='mainDish']")
veg_curry = dropdown_func("//select[@id='curry']")

#locate the radio button for Non-Vegetarian and click
nonveg = browser.find_element_by_xpath("//input[@name='foodType' and @value='nonveg']")
nonveg.click()

# retrieve maindish & Curry values
non_veg_main_dish = dropdown_func("//select[@id='mainDish']")
non_veg_curry = dropdown_func("//select[@id='curry']")

#print the options
print ('Veg Main Dish \n', veg_main_dish)
print ('Veg Curry \n', veg_curry)
print ('Non Veg Main Dish \n', non_veg_main_dish)
print ('Non Veg Curry \n', non_veg_curry)
    
#close browser
browser.close()    



