from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
import time
import os

desired_caps = {# UiAutomator2 UiAutomator1 Espresso
    "automationName" : "UiAutomator2",
    "deviceName": "Moto Z3 Play",
    "platformName": "Android",
    "app": 'F:/AGTGA/posifon.apk',
    "appWaitActivity" : ".*"
}
print("banana1")

port = 'http://localhost:4723/wd/hub'

print("banana2")

driver = webdriver.Remote(command_executor=port, desired_capabilities=desired_caps)

print("banana3")


#canStartNew = selenium.webdriver.common.utils.is_url_connectable(port) ##returns bool to check it can create a new session
#print(canStartNew)

activity = driver.current_activity ##get current activity
print(activity)

#el = driver.find_elements_by_accessibility_id("inputA")
#print(el)

source = driver.page_source
print(source)

file1 = open("source.txt","w+") 

file1.write(source)

file1 = open("source.txt","a") 
file1.close() 
##
#inputA = WebDriverWait(driver, 30).until(
#    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "inputA"))
#)
#inputA.send_keys("10")
#
#inputB = WebDriverWait(driver, 30).until(
#    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "inputB"))
#)
#inputB.send_keys("5")
#
#sum = WebDriverWait(driver, 30).until(
#    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "sum"))
#)
#el = driver.find_elements_by_accessibility_id(activity)
#print(el)
#if sum!=None and sum.text=="15":
#  print("TRUE everything worked")
#else:
#  print("FALSE we did not get 15")


print("Exiting program")
driver.quit()