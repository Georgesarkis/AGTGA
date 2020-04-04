import os
import time
from Algo.Helpers.InformationHolder import getActionCount, setActionCount, getCount, getDesiredCap


def AppendToLog(log):
    print(log)
    log = log + "\n"
    file1 = open("F:/AGTGA/ScreenShots/log" + str(getCount()) + ".txt", "a")
    file1.write(log)
    file1.close()


def TakeScreenShot(t, driver):
    TestCaseCount = str(getCount())
    _actionCount = getActionCount()
    time.sleep(t)
    path = "F:/AGTGA/ScreenShots/" + TestCaseCount
    if not os.path.exists(path):
        os.makedirs(path)
    ScreenShotLocation = path + "/V" + str(_actionCount) + ".png"
    print(ScreenShotLocation)
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
    log = log + "time.sleep(5)\n"

    _testCaseCount = getCount()
    file1 = open("F:/AGTGA/TestSuite/TestSuite/TestCase" + str(_testCaseCount) + ".py", "w+")
    file1.write(log)
    file1.close()


def AppendCode(log):
    log = log + "\n"
    file1 = open("F:/AGTGA/TestSuite/TestSuite/TestCase" + str(getCount()) + ".py", "a")
    file1.write(log)
    file1.close()


def AppendDesiredCap():
    log = "{'automationName' : 'UiAutomator2','deviceName': '" + getDesiredCap()[
        "deviceName"] + "','platformName': 'Android',  'app': '" + getDesiredCap()[
              "app"] + "' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false'," \
                       "'noReset' : 'true' } "
    return log


def AppendCodeClickButton(el):
    AppendCode("time.sleep(5)")
    AppendCode("el = ElementFinder(driver, " + str(el.location["x"]) + "," + str(el.location["y"]) + ")")

    AppendCode("el.click()")


def AppendCodeBackButtonClick():
    global log
    AppendCode("driver.back()")
