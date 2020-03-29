import os

from appium import webdriver
from Algo.Algo import AlgoMain
from Algo.Classes.View import View
from Algo.Helpers.Generator import AppendToLog
from Algo.Helpers.Handler import FindElements
from Algo.Helpers.InformationHolder import *


def run(desired_caps, username, password, algo, durationToWait, TestServer):
    port = 'http://localhost:4723/wd/hub'
    setPort(port)
    setDesiredCap(desired_caps)
    setUsername(username)
    setPassword(password)
    setAlgo(algo)
    setDurationToWait(durationToWait)
    setTestServer(TestServer)
    Finished = False
    count = getCount()
    '''
    driver = webdriver.Remote(command_executor=port, desired_capabilities=desired_caps)
    CurrentView = NewView()
    print("run number: " + str(count))
    AlgoMain(driver, CurrentView, algo, username, password, durationToWait, _testCaseCount, TestServer)
'''
    while not Finished:
        setActionCount(0)
        try:
            driver = webdriver.Remote(command_executor=port, desired_capabilities=desired_caps)
            CurrentView = NewView(driver)
            print("run number: " + str(count))
            Finished = AlgoMain(driver, CurrentView, algo, username, password, durationToWait, TestServer)
            driver.quit()
            setCount(getCount() + 1)
        except Exception as e:
            print("Exception aquired with message: " + str(e))
            AppendToLog("Exception aquired with message: " + str(e))
            setCount(getCount() + 1)


def NewView(driver):
    # CreateLog
    ScreenShotLocation = CreateTheLog(driver)

    # Create new object from every single element group
    ButtonViewList = FindElements("ButtonView", driver)
    EditViewList = FindElements("EditView", driver)
    TextViewList = FindElements("TextView", driver)
    ImageViewList = FindElements("ImageView", driver)

    # Create new object for View
    ViewIDCount = 0
    return View(ViewIDCount, ScreenShotLocation, ImageViewList, TextViewList, EditViewList, ButtonViewList)


def CreateTheLog(driver):
    log = "New View Has been Created, The activity name is " + driver.current_activity +"\n"
    _testCaseCount = getCount()
    _actionCount = getActionCount()
    file1 = open("F:/AGTGA/ScreenShots/log" + str(_testCaseCount) + ".txt", "w+")
    file1.write(log)
    file1.close()
    path = "F:/AGTGA/ScreenShots/" + str(_testCaseCount)
    if not os.path.exists(path):
        os.makedirs(path)
    ScreenShotLocation = path + "/V" + str(_actionCount) + ".png"
    driver.get_screenshot_as_file(ScreenShotLocation)
    setActionCount(_actionCount + 1)
    return ScreenShotLocation

def CreateTheCode():
    log = "from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice \n"
    log = log + "device = MonkeyRunner.waitForConnection() \n"
    log = log + "device.installPackage('" + getDesiredCap()["app"] +"')"

    _testCaseCount = getCount()
    file1 = open("F:/AGTGA/ScreenShots/TestCase" + str(_testCaseCount) + ".py", "w+")
    file1.write(log)
    file1.close()