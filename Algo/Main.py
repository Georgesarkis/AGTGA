import sys

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
import time
import os
from Algo.Algo import AlgoMain
from Algo.Classes.ButtonView import ButtonView
from Algo.Classes.ImageView import ImageView
from Algo.Classes.EditView import EditView
from Algo.Classes.TextView import TextView
from Algo.Classes.View import View
from Algo.Helpers.ViewChecker import FindElements

CurrentView = None
driver = None
CurrentActivity = None
OldActivity = None
TestCaseCount = 0


def run(desired_caps, username, password, algo, durationToWait, TestServer):
    port = 'http://localhost:4723/wd/hub'
    global driver
    global Currentactivity
    global CurrentView
    global TestCaseCount
    banana = True
    count = 0

    '''while banana:
        try:'''
    driver = webdriver.Remote(command_executor=port, desired_capabilities=desired_caps)
    Currentactivity = driver.current_activity  ##get current activity
    NewView()
    print("run number: " + str(count))
    AlgoMain(driver, CurrentView, algo, username, password, durationToWait, TestCaseCount, TestServer)

    driver.quit()
    '''    except Exception as e:
            print("Exception aquired with message: " + str(e))
            count = count + 1
            print("do you want to stop?")
            input1 = input()
            banana = not (input1 == "y")
    '''

def NewView():
    # CreateLog
    ScreanShotlocation = CreateTheLog(driver)

    # Create new object from every single element group
    ButtonViewList = FindElements("ButtonView", driver)
    EditViewList = FindElements("EditView", driver)
    TextViewList = FindElements("TextView", driver)
    ImageViewList = FindElements("ImageView", driver)

    # Create new object for View
    global CurrentView
    ViewIDCount = 0
    CurrentView = View(ViewIDCount, ScreanShotlocation, ImageViewList, TextViewList, EditViewList, ButtonViewList)


def CreateTheLog(driver):
    log = "New View Has been Created, The activity name is " + driver.current_activity +"\n"
    global TestCaseCount
    file1 = open("F:/AGTGA/ScreenShots/log" + str(TestCaseCount) + ".txt", "w+")
    TestCaseCount = TestCaseCount + 1
    file1.write(log)
    file1.close()
    ViewIDCount = 0
    ScreenShotLocation = "F:/AGTGA/ScreenShots/" + "V" + str(ViewIDCount) + ".png"
    driver.get_screenshot_as_file(ScreenShotLocation)
    return ScreenShotLocation
