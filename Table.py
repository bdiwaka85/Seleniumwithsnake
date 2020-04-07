'''
Created on Apr 7, 2020

@author: Diwakar
'''
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome("D:\webdrivers\chromedriver.exe")
browser.maximize_window()
browser.get("https://www.seleniumeasy.com/test/")
browser.implicitly_wait(2)

#Navigate to the table from the navigation bar in the middle
lnktable = browser.find_element_by_xpath("//*[@id='navbar-brand-centered']/ul[1]/li[3]/a")
lnktable2 = browser.find_element_by_xpath("//*[@id='navbar-brand-centered']/ul[1]/li[3]/ul/li[5]/a")
actions = ActionChains(browser)
# the below action statement will navigate to the table directly.
actions.move_to_element(lnktable).click(lnktable).move_to_element(lnktable2).click(lnktable2).perform()

browser.minimize_window()
#find the table in the loaded page
table = browser.find_element_by_xpath("//table[@id='example']")

#retrieve the rows from the table using tr tag
rows = table.find_elements_by_tag_name("tr")

#to print all the column data in each row, iterate through the list of rows, find the column data with td tag.
#store the column data (webelement) in a list, iterate through the column list and capture the column data for each row

col_text = []
for row in range(1,len(rows)):
    cols = rows[row].find_elements_by_tag_name("td")
    each = [each.text for each in cols]
    col_text.append(each)

print(col_text)

#close browser
browser.close()

""" 
the below code is for reference to write the column details into a csv file.
import csv
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://example.com/")
table = driver.find_element_by_css_selector("#tableid")
with open('eggs.csv', 'w', newline='') as csvfile:
    wr = csv.writer(csvfile)
    for row in table.find_elements_by_css_selector('tr'):
        wr.writerow([d.text for d in row.find_elements_by_css_selector('td')])
"""
