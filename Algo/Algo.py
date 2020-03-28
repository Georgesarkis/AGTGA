import time

from Algo.Helpers.ViewChecker import ActivityChecker, ViewChecker, TakeScreenShot, AppendToLog, getActionCount, NewView, \
    ClickButton, setWaitTime, getViewList
from .LeakDetectionAlgo import LeakDetectionAlgo
from .ActionCoverageAlgo import ActionCoverageAlgo
from .StateCoverageAlgo import StateCoverageAlgo
from Algo.Classes.View import View
from Algo.Helpers.ViewChecker import FindElements

driver = None
CurrentView = None
successfullyLoggedin = False

def AlgoMain(_driver, _currentView, algo, username, password, durationToWait, _testCaseCount, TestServer):
    global driver, successfullyLoggedin, CurrentView
    global TestCaseCount
    CurrentView = _currentView
    Views = getViewList()
    Views.append(CurrentView)
    driver = _driver
    TestCaseCount = _testCaseCount
    setWaitTime(durationToWait)

    if username != "" and password != "":
        FillEditView(CurrentView.getEditViewList(), username, password)
        print("will press back button")
        driver.back()
        successfullyLoggedin = ClickLoginButton(driver, CurrentView.getButtonViewList())

    if successfullyLoggedin and TestServer:
        if ConnectToTestServer(driver):
            time.sleep(10)
            NewView(driver, CurrentView)
        else:
            time.sleep(10)
            NewView(driver, CurrentView)

    if algo == "StateCoverage":
        StateCoverageAlgo()

    elif algo == "ActionCoverage":
        ActionCoverageAlgo(driver, CurrentView)

    elif algo == "LeakDetection":
        LeakDetectionAlgo()


def FillEditView(editViewList, userName, password):
    global driver
    if len(editViewList) == 2:
        username = editViewList[0]
        AppendToLog("EditView with id: " + str(username.id) + " has been clicked and filled with string: " + userName)
        username.clicked = True
        username.click()
        username.send_keys(userName)
        TakeScreenShot(0, driver)
        Password = editViewList[1]
        AppendToLog("EditView with id: " + str(username.id) + " has been clicked and filled with string: " + password)
        Password.clicked = True
        Password.click()
        Password.send_keys(password)
        TakeScreenShot(0, driver)


def ClickLoginButton(driver, ButtonViewList):
    for el in ButtonViewList:
        if el.text.lower() == "login" or el.text.lower() == "signin" or el.text.lower() == "log in" or el.text.lower() == "sign in":
            return ClickButton(driver, el)


def ConnectToTestServer(driver):
    ButtonViewList = FindElements('ButtonView', driver)
    for el in ButtonViewList:
        if el.text.lower() == "yes":
            return ClickButton(driver, el)
    return False
