'''
Created on Apr 10, 2020

Below program opens an ecommerce website, searches for an item, add to cart and finishes all the way till order confirmation

### next steps to add, asserts check for quantity, price etc in cart page and assert checks in the address verificaiton page ###

@author: Balaji
'''
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

class test_ecom_order(unittest.TestCase):
    
    app_test = "http://automationpractice.com/index.php"
    
    #setUp Class
    def setUp(self):
        self.browser = webdriver.Chrome("D:\webdrivers\chromedriver.exe")
        self.browser.get(self.app_test)
        self.browser.maximize_window()
        self.browser.implicitly_wait(5) # adding implicit wait for 5 seconds
        
    #tearDown Class   
    def tearDown(self):
        self.browser.save_screenshot("D:\Balaji\SeleniumScreenshots\OrderConfirm.png")
        self.browser.quit()
    
    def test_Ecom_Order(self):
        self.browser.find_element_by_id("search_query_top").send_keys("Printed Summer Dress")
        self.browser.find_element_by_xpath("//*[@id='searchbox']/button").click()
        wait = WebDriverWait(self.browser, 2)
        wait.until(ec.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Chiffon")))
        self.browser.find_element_by_partial_link_text("Chiffon").click()
#product page
        self.browser.find_element_by_id("quantity_wanted").clear()
        self.browser.find_element_by_id("quantity_wanted").send_keys("2")
        size = Select(self.browser.find_element_by_xpath("//select[@id='group_1']"))
        size.select_by_value("2")
        self.browser.find_element_by_xpath("//*[@id='color_16']").click()
        self.browser.find_element_by_xpath("//*[@id='add_to_cart']/button/span").click() 
#overlay in the product page
        self.browser.implicitly_wait(5) # this is to wait for the overlay to load, it is not like an alert
        self.browser.find_element_by_partial_link_text("Proceed").click()
#Shopping Cart
        wait.until(ec.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "checkout")))
        self.browser.find_element_by_partial_link_text("checkout").click()
#Account Creation Page        
        wait.until(ec.element_to_be_clickable((By.ID, "SubmitCreate")))
        self.browser.find_element_by_xpath("//input[@id='email_create']").send_keys("some4@somewhere.com")
        self.browser.find_element_by_id("SubmitCreate").click()
#Customer Registration Details
        self.browser.find_element_by_xpath("//input[@id='id_gender1' and @type = 'radio']").click()
        self.browser.find_element_by_xpath("//input[@id='customer_firstname']").send_keys("First")
        self.browser.find_element_by_xpath("//input[@id='customer_lastname']").send_keys("Last")
        self.browser.find_element_by_xpath("//input[@id='passwd']").send_keys("test123")
        dob_days = Select(self.browser.find_element_by_xpath("//select[@id='days']"))
        dob_days.select_by_value("15")
        self.browser.implicitly_wait(2)
        dob_month = Select(self.browser.find_element_by_xpath("//select[@id='months']"))
        dob_month.select_by_value("5")
        self.browser.implicitly_wait(2)
        dob_year = Select(self.browser.find_element_by_xpath("//select[@id='years']"))
        dob_year.select_by_value("1990")
        self.browser.find_element_by_xpath("//input[@id='firstname']").clear()
        self.browser.find_element_by_xpath("//input[@id='firstname']").send_keys("John")
        self.browser.find_element_by_xpath("//input[@id='lastname']").clear()
        self.browser.find_element_by_xpath("//input[@id='lastname']").send_keys("Doe")
        self.browser.find_element_by_xpath("//input[@id='address1']").send_keys("124 First Street")
        self.browser.find_element_by_xpath("//input[@id='city']").send_keys("Hoffman Estates")
        id_state = Select(self.browser.find_element_by_xpath("//select[@id='id_state']"))
        id_state.select_by_value("13")
        self.browser.find_element_by_xpath("//input[@id='postcode']").send_keys("60169")
        self.browser.find_element_by_xpath("//input[@id='phone_mobile']").send_keys("9897654321")
        self.browser.find_element_by_xpath("//button[@id='submitAccount']").click()
#Address Verification Page
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='center_column']/form/p/button")))
        self.browser.find_element_by_xpath("//*[@id='center_column']/form/p/button").click()
#Shipping Method, T&C checkbox
        wait.until(ec.element_to_be_clickable((By.XPATH, "//form[@id='form']/p/button")))
        self.browser.find_element_by_xpath("//input[@id='cgv']").click()
        self.browser.find_element_by_xpath("//form[@id='form']/p/button").click()
#Payment Selection
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='HOOK_PAYMENT']/div[2]/div/p/a")))
        self.browser.find_element_by_xpath("//*[@id='HOOK_PAYMENT']/div[2]/div/p/a").click()
#Final Confirmation
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='center_column']/form/p/button")))
        self.browser.find_element_by_xpath("//*[@id='center_column']/form/p/button").click()
#Order Confirmation
        self.browser.implicitly_wait(2)
        success = self.browser.find_element_by_xpath("//*[@id='center_column']/p").text
        assert "complete" in success
       
if __name__ == "__main__":
    unittest.main()
        