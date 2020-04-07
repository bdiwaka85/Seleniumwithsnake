'''
Created on Apr 7, 2020
This program opens the given website logs in as Admin, navigates to the  page through mouse hover, fills the form to get generate the table and prints the data
@author: Balaji
'''
#all imports
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains

class test_webtable(unittest.TestCase):
    
    App_Test = "https://opensource-demo.orangehrmlive.com/"
    
#setup class 
    def setUp(self):
        self.browser = webdriver.Chrome("D:\webdrivers\chromedriver.exe")
        self.browser.get(self.App_Test)
        self.browser.maximize_window()

#tearDown class         
    def tearDown(self):
        welcome = self.browser.find_element_by_xpath('//*[@id="welcome"]')
        logout = self.browser.find_element_by_xpath("//*[@id='welcome-menu']/ul/li[2]/a")
        actions = ActionChains(self.browser)
        actions.move_to_element(welcome).click(welcome).move_to_element(logout).click(logout).perform()
        self.browser.implicitly_wait(3)
        self.browser.close()
        
#main module
    def test_webtable_print(self):
#login
        self.browser.find_element_by_id("txtUsername").send_keys("Admin")
        self.browser.find_element_by_id("txtPassword").send_keys("admin123")
        self.browser.find_element_by_xpath("//input[@id='btnLogin']").click()
#navigate using mousehover
        time = self.browser.find_element_by_xpath("//*[@id='menu_time_viewTimeModule']")
        reports = self.browser.find_element_by_xpath("//*[@id='menu_time_Reports']")
        summary = self.browser.find_element_by_xpath("//*[@id='menu_time_displayAttendanceSummaryReportCriteria']")
        actions = ActionChains(self.browser)
        actions.move_to_element(time).move_to_element(reports).move_to_element(summary).click().perform()
#fill the form to get the table
        self.browser.find_element_by_xpath("//form//input[@id='employee_name']").send_keys("All")
        self.browser.find_element_by_xpath("//form//input[@id='from_date']").clear()
        self.browser.find_element_by_xpath("//form//input[@id='from_date']").send_keys("2020-01-01")
        self.browser.find_element_by_xpath("//form//input[@id='to_date']").clear()
        self.browser.find_element_by_xpath("//form//input[@id='to_date']").send_keys("2020-01-31")
        self.browser.find_element_by_xpath("//form//input[@id='viewbutton']").click()
#find the table in the loaded page
        table = self.browser.find_element_by_xpath("//table[@id='resultTable']")
#retrieve the rows from the table using tr tag
        rows = table.find_elements_by_tag_name("tr")
        rows = rows[:-1]
#print the table data
        cols_text = []
        for row in range(1,len(rows)):
            cols = rows[row].find_elements_by_tag_name("td")
            each = [each.text for each in cols]
            cols_text.append(each)
        print (cols_text)
                
if __name__ == '__main__':
    unittest.main()