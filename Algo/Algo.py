import time

from Algo.Helpers.ViewChecker import ActivityChecker, ViewChecker
from .LeakDetectionAlgo import LeakDetectionAlgo
from .ActionCoverageAlgo import ActionCoverageAlgo
from .StateCoverageAlgo import StateCoverageAlgo

driver = None
ViewIDCount = 1
TestCaseCount = 0

def AlgoMain(_driver, currentView, algo, username, password, durationToWait, _testCaseCount):
    global  driver
    global TestCaseCount
    driver = _driver
    TestCaseCount = _testCaseCount

    if username != "" and password != "":
        FillEditView(currentView.getEditViewList(), username, password)
        driver.back()
        successfullyLoggedin = not ClickLoginButton(currentView.getButtonViewList())

    if algo == "StateCoverage":
        StateCoverageAlgo()

    elif algo == "ActionCoverage":
        ActionCoverageAlgo()

    elif algo == "LeakDetection":
        LeakDetectionAlgo()


def FillEditView(editViewList, userName, password):
    if len(editViewList) == 2:
        username = editViewList[0]
        AppendToLog("EditView with id: " + str(username.id) + " has been clicked and filled with string: " + userName)
        username.click()
        username.send_keys(userName)
        TakeScreenShot(0)
        Password = editViewList[1]
        AppendToLog("EditView with id: " + str(username.id) + " has been clicked and filled with string: " + password)
        Password.click()
        Password.send_keys(password)
        TakeScreenShot(0)


def ClickLoginButton(ButtonViewList):
    for el in ButtonViewList:
        if el.text.lower() == "login" or el.text.lower() == "signin" or el.text.lower() == "log in" or el.text.lower() == "sign in":
            return ClickButton(el)


def AppendToLog(log):
    global TestCaseCount

    log = log + "\n"
    file1 = open("F:/AGTGA/ScreenShots/log" + str(TestCaseCount) + ".txt", "a")
    file1.write(log)
    file1.close()


def TakeScreenShot(t):
    global driver
    global ViewIDCount
    time.sleep(t)
    ScreenShotLocation = "F:/AGTGA/ScreenShots/" + "V" + str(ViewIDCount) + ".png"
    ViewIDCount = ViewIDCount + 1
    driver.get_screenshot_as_file(ScreenShotLocation)
    return ScreenShotLocation


def ClickButton(el):
    global driver

    AppendToLog("button with id: " + str(el.id) + " with string value: " + el.text + " has been clicked")
    oldActivity = driver.current_activity
    el.click()
    TakeScreenShot(1)
    driver.implicitly_wait(5000)
    if ActivityChecker(oldActivity, driver.current_activity):
        global ViewIDCount
        ScreenShotLocation1 = "F:/AGTGA/ScreenShots/" + "V" + str(ViewIDCount - 1) + ".png"
        ScreenShotLocation2 = "F:/AGTGA/ScreenShots/" + "V" + str(ViewIDCount - 2) + ".png"
        return ViewChecker(ScreenShotLocation1, ScreenShotLocation2)

    return False
