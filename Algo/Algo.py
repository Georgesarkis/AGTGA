import time
from Algo.Helpers.Generator import AppendToLog
from Algo.Helpers.Handler import *
from Algo.Helpers.InformationHolder import *
from .ActionCoverageAlgo import ActionCoverageAlgo

driver = None
CurrentView = None
successfullyLoggedin = False


def AlgoMain(_driver, _currentView, algo, username, password, durationToWait, TestServer):
    global driver, successfullyLoggedin, CurrentView
    CurrentView = _currentView
    Views = getViewList()
    Views.append(CurrentView)
    setActivity(_driver.current_activity)
    driver = _driver
    setWaitTime(durationToWait)
    SetUsername(username)
    SetPassword(password)
    SetRootView(CurrentView)

    if username != "" and password != "":
        FillEditView(_driver,CurrentView.getEditViewList(), username, password)

        if ClickLoginButton(driver, _currentView.ButtonViewList, _currentView.TextViewList) and TestServer:
            if ConnectToTestServer(driver):
                time.sleep(10)
                CurrentView = NewView(driver, CurrentView)
            else:
                print("something bad happend when trying to connect to test server")
                time.sleep(10)
                CurrentView = NewView(driver, CurrentView)
        else:
            time.sleep(10)
            CurrentView = NewView(driver, CurrentView)
    else:
        time.sleep(10)
        CurrentView = NewView(driver, CurrentView)
    print("the algo value is")
    print(algo)
    if algo == "ActionCoverage":
        setLeakDetection(False)
        return ActionCoverageAlgo(driver, CurrentView)

    elif algo == "LeakDetection":
        setLeakDetection(True)
        return ActionCoverageAlgo(driver, CurrentView)


def ConnectToTestServer(driver):
    ButtonViewList = FindElements('ButtonView', driver)
    for el in ButtonViewList:
        if el.text.lower() == "yes" or el.text.lower() == "ja":
            return ClickButton(driver, el)
    return False
