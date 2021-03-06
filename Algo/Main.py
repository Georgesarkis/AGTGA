import os

from appium import webdriver
from Algo.Algo import AlgoMain
from Algo.Classes.View import View
from Algo.Helpers.Generator import AppendToLog, CreateTheCode
from Algo.Helpers.Handler import FindElements
from Algo.Helpers.InformationHolder import *


def run(desired_caps, username, password, algo, durationToWait, TestServer, Verbose, ApplicationID):
    port = 'http://localhost:4723/wd/hub'
    Finished = False
    setDesiredCap(desired_caps)
    setVerbose(Verbose)
    count = getCount()
    SetApplicationID(ApplicationID)
    ''' this is used in testing environment, to not go in while loop and try catch, to get more detailed explanation about the crash of the tool(AGTGA) not the app'''
    '''
    CreateTheCode()
    driver = webdriver.Remote(command_executor=port, desired_capabilities=desired_caps)
    CurrentView = NewView(driver)
    print("run number: " + str(count))
    AlgoMain(driver, CurrentView, algo, username, password, durationToWait, TestServer)
    '''
    while not Finished:
        setActionCount(0)
        CreateTheCode()
        try:
            driver = webdriver.Remote(command_executor=port, desired_capabilities=desired_caps)
            CurrentView = NewView(driver)
            if getVerbose(): print("run number: " + str(count))
            Finished = AlgoMain(driver, CurrentView, algo, username, password, durationToWait, TestServer)
            driver.press_keycode(3)
            driver.close_app()
            driver.quit()
            setCount(getCount() + 1)
        except Exception as e:
            if getVerbose(): print("Exception aquired with message: " + str(e))
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
    ImageButtonList = FindElements("ImageButton", driver)
    CheckedTextList = FindElements("CheckedTextView", driver)
    # Create new object for View
    ViewIDCount = 0
    return View(ViewIDCount, ScreenShotLocation, ImageViewList, TextViewList, EditViewList, ButtonViewList, ImageButtonList, CheckedTextList)


def CreateTheLog(driver):
    log = "New View Has been Created, The activity name is " + driver.current_activity + "\n"
    _testCaseCount = getCount()
    _actionCount = getActionCount()
    file1 = open(os.getcwd() + "/ScreenShots/log" + str(_testCaseCount) + ".txt", "w+")
    file1.write(log)
    file1.close()
    path = os.getcwd() + "/ScreenShots/" + str(_testCaseCount)
    if not os.path.exists(path):
        os.makedirs(path)
    ScreenShotLocation = path + "/V" + str(_actionCount) + ".png"
    driver.get_screenshot_as_file(ScreenShotLocation)
    setActionCount(_actionCount + 1)
    return ScreenShotLocation
