from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
import time
import os
import sys
sys.path.insert(1, '../Classes')
from .ButtonView import ButtonView
from .EditView import EditView
from .ImageView import ImageView
from .TextView import TextView
from .View import View
from .Algo import *

CurrentView = None
driver = None
CurrentActivity = None
OldActivity = None
TestCaseCount = 0
ViewIDCount = 0


def run(desired_caps):
    port = 'http://localhost:4723/wd/hub'
    global driver
    driver = webdriver.Remote(command_executor=port, desired_capabilities=desired_caps)

    global Currentactivity
    Currentactivity = driver.current_activity  ##get current activity
    NewView()


def FindElements(ClassType):
    List = []
    if (ClassType == "ButtonView"):
        elements = driver.find_elements_by_class_name('android.widget.Button')
        for el in elements:
            ID = el.id
            locationX = el.locaiton["x"]
            locationY = el.locaiton["y"]
            ButtonView = ButtonView(ID, True, locationX, locationY)
            List.append(ButtonView)

    elif (ClassType == "EditView"):
        elements = driver.find_elements_by_class_name('android.widget.EditText')
        for el in elements:
            ID = el.id
            locationX = el.locaiton["x"]
            locationY = el.locaiton["y"]
            EditText = EditText(ID, True, locationX, locationY)
            List.append(EditText)

    elif (ClassType == "TextView"):
        elements = driver.find_elements_by_class_name('android.widget.TextView')
        for el in elements:
            ID = el.id
            locationX = el.locaiton["x"]
            locationY = el.locaiton["y"]
            TextView = TextView(ID, True, locationX, locationY)
            List.append(TextView)

    elif (ClassType == "ImageView"):
        elements = driver.find_elements_by_class_name('android.widget.ImageView')
        for el in elements:
            ID = el.id
            locationX = el.locaiton["x"]
            locationY = el.locaiton["y"]
            ImageView = ImageView(ID, True, locationX, locationY)
            List.append(ImageView)

    return List


def NewView():
    # TakeScreenShot
    global driver
    screenshotBase64 = driver.get_screenshot_as_base64()
    global ViewIDCount
    ScreanShotlocation = "F:/AGTGA/ScreenShots/" + "V" + ViewIDCount + ".png"
    screenshotBase64.save(ScreanShotlocation)

    # CreateLog
    CreateTheLog(driver)

    # Create new object from every single element group
    ButtonViewList = FindElements("ButtonView")
    EditViewList = FindElements("EditView")
    TextViewList = FindElements("TextView")
    ImageViewList = FindElements("ImageView")

    # Create new object for View
    global CurrentView
    CurrentView = View(ViewIDCount, ScreanShotlocation, ImageViewList, TextViewList, EditViewList, ButtonViewList)


def CreateTheLog(driver):
    log = "New View Has been Created, The activity name is " + driver.current_activity + "\n"
    global TestCaseCount
    file1 = open("F:/AGTGA/log" + TestCaseCount + ".txt", "w+")
    file1.write(log)
    file1.close()


def AppendToLog(log):
    global TestCaseCount
    file1 = open("F:/AGTGA/log" + TestCaseCount + ".txt", "a")
    file1.write(log)
    file1.close()
