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
    "app": 'F:/AGTGA/APKS/posifon.apk',
    "autoGrantPermissions" : "true",
    "appWaitActivity" : "*.*",#"md5dccfc7716c9297b278a85628ec83026a.LoginActivity"
    #"appActivity" : ".*",
    "fullreset": "false",
     "noReset": "true"
}

port = 'http://localhost:4723/wd/hub'
driver = webdriver.Remote(command_executor=port, desired_capabilities=desired_caps)

time.sleep(10)

#canStartNew = selenium.webdriver.common.utils.is_url_connectable(port) ##returns bool to check it can create a new session
#print(canStartNew)
"""
print(driver.query_app_state('io.appium.android.apis'))
driver.orientation = "LANDSCAPE"
print("land")
activity = driver.current_activity ##get current activity
print(activity)
time.sleep(10)
activity = driver.current_activity ##get current activity
print(activity)
print(driver.query_app_state('io.appium.android.apis'))
driver.orientation = "PORTRAIT"
print("port")
time.sleep(10)
driver.orientation = "LANDSCAPE"
print("land")"""
time.sleep(10)

activity = driver.current_activity ##get current activity
print(activity)
print(driver.query_app_state('io.appium.android.apis'))
print("before background")

driver.background_app(10)
print("background")
activity = driver.current_activity ##get current activity
print(activity)
print(driver.query_app_state('io.appium.android.apis'))

time.sleep(10)
activity = driver.current_activity ##get current activity
print(activity)
print(driver.query_app_state('io.appium.android.apis'))

#el = driver.find_elements_by_accessibility_id("inputA")
#print(el)
"""
source = driver.page_source
#print(source)

file1 = open("source.txt","w+") 

file1.write(source)

file1 = open("source.txt","a") 
print("saved the three to the file")
file1.close() 
element = driver.find_element_by_id("posifon.Care:id/username")
element.click()
element.send_keys("demo4@konto.se")
print("entered username")

element = driver.find_element_by_id("posifon.Care:id/password")
element.click()
element.send_keys("Sommar2018")
print("entered password")



element = driver.find_elements_by_class_name('android.widget.Button')

print(driver)

for el in element:
    print("found element:")
    print(el.id)
    el.click()
    print("clicked login")

print(driver)

driver.implicitly_wait(5000)

element = driver.find_element_by_id("android:id/button1")
element.click()

source = driver.page_source
file1 = open("source1.txt","w+")
file1.write(source)
file1 = open("source1.txt","a")
print("saved the three to the file")
file1.close()
screenshotBase64 = driver.get_screenshot_as_base64()
screenshotBase64.save("source1.png")

while(activity == driver.current_activity):
    driver.implicitly_wait(5000)


activity1 = driver.current_activity ##get current activity
print(activity1)

driver.implicitly_wait(5000)

source = driver.page_source
file1 = open("source2.txt","w+") 
file1.write(source)
file1 = open("source2.txt","a") 
print("saved the three to the file")
file1.close() 
screenshotBase64 = driver.get_screenshot_as_base64()
screenshotBase64.save("source2.png")






list = driver.find_element_by_id("posifon.Care:id/myExpandableListview")
print(list)
list.click()
print("myExpandableListview clicked")

input1 = ""
while(input1 != "n"):
    driver.implicitly_wait(5000)
    input1 = input()

source = driver.page_source
file1 = open("source3.txt","w+") 
file1.write(source)
file1 = open("source3.txt","a") 
print("saved the three to the file")
file1.close() 
screenshotBase64 = driver.get_screenshot_as_base64()
screenshotBase64.save("source3.png")

activity1 = driver.current_activity ##get current activity
print(activity1)

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

"""

print("Exiting program")
driver.quit()