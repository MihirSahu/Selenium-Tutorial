#!/usr/bin/env python3
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#Download the driver for the browser that you want to use as a selenium driver. Get it from the browser website and add it to the PATH in the code level, not system level

driver = webdriver.Chrome()

#Click button
"""
#Use .get() to specify the website
driver.get("https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html")

#Use .implicitly_wait() to wait if element is not loaded. If it is, it runs next code immediately. The wait is set for the entire project, and is invoked whenever we try to find an element
driver.implicitly_wait(3)

#Use to find element by id, returns an object
my_element = driver.find_element_by_id('downloadButton')
#Use .click() to click on the element specified
my_element.click()

#Use to find element by class name
#progress_element = driver.find_element_by_class_name('progress-label')

#Use these to wait until the specified element is loaded before continuing
WebDriverWait(driver, 30).until(
    #Arguments: Element filtration, expected text
    EC.text_to_be_present_in_element(
        #By is another way to find elements
        (By.CLASS_NAME, 'progress-label'),
        'Complete!'
    )
)
"""

#Type characters
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
driver.implicitly_wait(5)

sum1 = driver.find_element_by_id('sum1')
sum2 = driver.find_element_by_id('sum2')

#Use .send_keys() to specify what text to send
sum1.send_keys(15)
sum2.send_keys(15)
#To send keys directly use .send_keys(Keys.<key name>). Make sure to import 'from selenium.webdriver.common.keys import Keys'

#Use to select elements by specified attribute. The html pattern is '<tag>[<attribute>="<value>"]'
btn = driver.find_element_by_css_selector('button[onclick="return total()"]')
btn.click()
