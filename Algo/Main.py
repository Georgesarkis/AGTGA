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

CurrentView = None
driver = None
CurrentActivity = None
OldActivity = None
TestCaseCount = 0

def run(desired_caps, username, password, algo, durationToWait):
    port = 'http://localhost:4723/wd/hub'
    global driver
    driver = webdriver.Remote(command_executor=port, desired_capabilities=desired_caps)

    global Currentactivity
    Currentactivity = driver.current_activity  ##get current activity
    NewView()

    global CurrentView
    global TestCaseCount
    AlgoMain(driver, CurrentView, algo, username, password, durationToWait, TestCaseCount)

def FindElements(ClassType):
    List = []
    if (ClassType == "ButtonView"):
        elements = driver.find_elements_by_class_name('android.widget.Button')
        for el in elements:
            ID = el.id
            locationX = el.location["x"]
            locationY = el.location["y"]
            Button = ButtonView(ID, True, locationX, locationY)
            List.append(Button)

    elif (ClassType == "EditView"):
        elements = driver.find_elements_by_class_name('android.widget.EditText')
        for el in elements:
            ID = el.id
            locationX = el.location["x"]
            locationY = el.location["y"]
            Edit = EditView(ID, True, locationX, locationY)
            List.append(Edit)

    elif (ClassType == "TextView"):
        elements = driver.find_elements_by_class_name('android.widget.TextView')
        for el in elements:
            ID = el.id
            locationX = el.location["x"]
            locationY = el.location["y"]
            Text = TextView(ID, True, locationX, locationY)
            List.append(Text)

    elif (ClassType == "ImageView"):
        elements = driver.find_elements_by_class_name('android.widget.ImageView')
        for el in elements:
            ID = el.id
            locationX = el.location["x"]
            locationY = el.location["y"]
            Image = ImageView(ID, True, locationX, locationY)
            List.append(Image)

    return elements


def NewView():
    # CreateLog
    ScreanShotlocation = CreateTheLog(driver)

    # Create new object from every single element group
    ButtonViewList = FindElements("ButtonView")
    EditViewList = FindElements("EditView")
    TextViewList = FindElements("TextView")
    ImageViewList = FindElements("ImageView")

    # Create new object for View
    global CurrentView
    ViewIDCount = 0
    CurrentView = View(ViewIDCount, ScreanShotlocation, ImageViewList, TextViewList, EditViewList, ButtonViewList)


def CreateTheLog(driver):
    log = "New View Has been Created, The activity name is " + driver.current_activity + "\n"
    global TestCaseCount
    file1 = open("F:/AGTGA/ScreenShots/log" + str(TestCaseCount) + ".txt", "w+")
    file1.write(log)
    file1.close()
    ViewIDCount = 0
    ScreenShotLocation = "F:/AGTGA/ScreenShots/" + "V" + str(ViewIDCount) + ".png"
    driver.get_screenshot_as_file(ScreenShotLocation)
    return ScreenShotLocation
