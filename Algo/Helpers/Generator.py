import os
import time
from Algo.Helpers.InformationHolder import *


def AppendToLog(log):
    if getVerbose(): print(log)
    log = log + "\n"
    file1 = open(os.getcwd() + "/ScreenShots/log" + str(getCount()) + ".txt", "a")
    file1.write(log)
    file1.close()


def TakeScreenShot(t, driver):
    TestCaseCount = str(getCount())
    _actionCount = getActionCount()
    AddNumberOfActionsInThisTestCase()
    time.sleep(t)
    path = os.getcwd() + "/ScreenShots/" + TestCaseCount
    if not os.path.exists(path):
        os.makedirs(path)
    ScreenShotLocation = path + "/V" + str(_actionCount) + ".png"
    if getVerbose(): print(ScreenShotLocation)
    setActionCount(_actionCount + 1)
    driver.get_screenshot_as_file(ScreenShotLocation)
    return ScreenShotLocation


def CreateTheCode():
    log = "import time \n"
    log = log + "from appium import webdriver \n"
    log = log + "from appium.webdriver.common.touch_action import TouchAction  \n"
    log = log + "from TestSuite.TestSuiteHelper import ElementFinder \n \n \n"
    log = log + "port = 'http://localhost:4723/wd/hub' \n"
    log = log + "driver = webdriver.Remote(command_executor=port, desired_capabilities=" + AppendDesiredCap() + ") \n \n"
    log = log + "time.sleep(2)\n"

    _testCaseCount = getCount()
    strTestCaseCount = 00
    if _testCaseCount == 0:
        strTestCaseCount = "00"
    elif _testCaseCount == 1:
        strTestCaseCount = "01"
    elif _testCaseCount == 2:
        strTestCaseCount = "02"
    elif _testCaseCount == 3:
        strTestCaseCount = "03"
    elif _testCaseCount == 4:
        strTestCaseCount = "04"
    elif _testCaseCount == 5:
        strTestCaseCount = "05"
    elif _testCaseCount == 6:
        strTestCaseCount = "06"
    elif _testCaseCount == 7:
        strTestCaseCount = "07"
    elif _testCaseCount == 8:
        strTestCaseCount = "08"
    elif _testCaseCount == 9:
        strTestCaseCount = "09"
    else:
        strTestCaseCount = str(_testCaseCount)
    file1 = open(os.getcwd() + "/TestSuite/TestSuite/TestCase" + strTestCaseCount + ".py", "w+")
    file1.write(log)
    file1.close()


def AppendCode(log):
    _testCaseCount = getCount()
    strTestCaseCount = 00
    if _testCaseCount == 0:
        strTestCaseCount = "00"
    elif _testCaseCount == 1:
        strTestCaseCount = "01"
    elif _testCaseCount == 2:
        strTestCaseCount = "02"
    elif _testCaseCount == 3:
        strTestCaseCount = "03"
    elif _testCaseCount == 4:
        strTestCaseCount = "04"
    elif _testCaseCount == 5:
        strTestCaseCount = "05"
    elif _testCaseCount == 6:
        strTestCaseCount = "06"
    elif _testCaseCount == 7:
        strTestCaseCount = "07"
    elif _testCaseCount == 8:
        strTestCaseCount = "08"
    elif _testCaseCount == 9:
        strTestCaseCount = "09"
    else:
        strTestCaseCount = str(_testCaseCount)
    log = log + "\n"
    file1 = open(os.getcwd() + "/TestSuite/TestSuite/TestCase" + strTestCaseCount + ".py", "a")
    file1.write(log)
    file1.close()


def AppendDesiredCap():
    log = "{'automationName' : 'UiAutomator2','deviceName': '" + getDesiredCap()[
        "deviceName"] + "','platformName': 'Android',  'app': '" + getDesiredCap()[
              "app"] + "' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false'," \
                       "'noReset' : 'true' } "
    return log


def AppendCodeClickButton(el):
    AddLenghtOfTestCase()
    s = "time.sleep(2) \n"
    s = s + "el = ElementFinder(driver, " + str(el.location["x"]) + "," + str(el.location["y"]) + ") \n"
    s = s + "el.click()"
    AppendCode(s)


def AppendCodeBackButtonClick():
    AddLenghtOfTestCase()
    AppendCode("driver.back()")


def AppendCodeEditText(el, str):
    AppendCodeClickButton(el)
    s = "el.send_keys('" + str + "') \n"
    AppendCode(s)


def AppendCodeLeakDetectionBackground():
    AppendCode('driver.background_app(1)')


def AppendCodeLeakDetectionRotation():
    AppendCode('driver.orientation = "LANDSCAPE"')
    AppendCode('driver.orientation = "PORTRAIT"')
