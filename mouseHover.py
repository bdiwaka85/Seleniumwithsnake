'''
Created on Apr 6, 2020

code to mouserHover and click

@author: Balaji
'''
#import the webdriver
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome("D:\webdrivers\chromedriver.exe")
browser.maximize_window()
browser.get("https://opensource-demo.orangehrmlive.com/")

#login
browser.find_element_by_id("txtUsername").send_keys("Admin")
browser.find_element_by_id("txtPassword").send_keys("admin123")
browser.find_element_by_xpath("//input[@id='btnLogin']").click()

#identify the drop down using XPATH
hover_elemnt = browser.find_element_by_xpath("//ul/li/a[@id='menu_admin_viewAdminModule']")
hover_elemnt_2 = browser.find_element_by_xpath("//ul/li/a[@id='menu_admin_UserManagement']")
clk_elemnt = browser.find_element_by_xpath("//ul/li/a[@id='menu_admin_viewSystemUsers']")
actions = ActionChains(browser)
# 3 elements are being moved to in one step. it is same as navigating with the mouse. '.click().perform()' is the action which clicks proceeds to the link
actions.move_to_element(hover_elemnt).move_to_element(hover_elemnt_2).move_to_element(clk_elemnt).click().perform()

#close browser
browser.close()