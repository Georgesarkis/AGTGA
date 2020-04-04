import os
import time

from appium.webdriver.common.touch_action import TouchAction
from Algo.Classes.View import View
from Algo.Helpers.Generator import AppendToLog, TakeScreenShot, AppendCodeClickButton, AppendCodeBackButtonClick
from Algo.Helpers.InformationHolder import getActionCount, getViewList, getWaitTime, getCount, getLeakDetection
from Algo.Helpers.ViewChecker import ActivityChecker, ViewChecker
from Algo.LeakDetectionAlgo import LeakDetectionAlgo


def NewView(driver, CurrentView):
    Views = getViewList()
    ActionCount = getActionCount()
    TestCaseCount = str(getCount())

    path = "F:/AGTGA/ScreenShots/" + TestCaseCount
    if not os.path.exists(path):
        os.makedirs(path)
    AppendToLog("new View has been created with view id: " + str(CurrentView.SelfID + 1))
    ScreenShotLocation = path + "/V" + str(ActionCount - 1) + ".png"
    ButtonViewList = FindElements('ButtonView', driver)
    EditViewList = FindElements('EditView', driver)
    TextViewList = FindElements('TextView', driver)
    ImageViewList = FindElements('ImageView', driver)
    ImageButtonList = FindElements("ImageButton", driver)
    # Create new object for View
    ViewIDCount = CurrentView.SelfID + 1
    CurrentView = View(ViewIDCount, ScreenShotLocation, ImageViewList, TextViewList, EditViewList, ButtonViewList, ImageButtonList)
    print("new view is created with screenshot location: " + ScreenShotLocation)
    Views.append(CurrentView)
    print("Views list size: " + str(len(Views)))

    if getLeakDetection():
        LeakDetectionAlgo(driver)

    return CurrentView


def ClickBackButton(driver):
    AppendCodeBackButtonClick()
    driver.back()


def ClickButton(driver, el):
    if el is None:
        return False
    AppendCodeClickButton(el)
    WaitTime = getWaitTime()
    el.clicked = True
    AppendToLog("button with id: " + str(el.id) + "with location: " + str(el.location["x"]) +","+ str(el.location["y"])+  " with string value: " + el.text + " has been clicked")
    oldActivity = driver.current_activity
    el.click()
    time.sleep(WaitTime)
    TakeScreenShot(0, driver)
    if ActivityChecker(oldActivity, driver.current_activity):
        ActionCount = getActionCount()
        ScreenShotLocation1 = "F:/AGTGA/ScreenShots/" + str(getCount()) + "/V" + str(ActionCount - 2) + ".png"
        ScreenShotLocation2 = "F:/AGTGA/ScreenShots/" + str(getCount()) + "/V" + str(ActionCount - 1) + ".png"
        return ViewChecker(ScreenShotLocation1, ScreenShotLocation2)
    return True


def FindElements(ClassType, driver):
    source = driver.page_source

    List = []
    if ClassType == "ButtonView":
        if "Button" in source:
            List = driver.find_elements_by_class_name('android.widget.Button')

    elif ClassType == "EditView":
        if "EditText" in source:
            List = driver.find_elements_by_class_name('android.widget.EditText')

    elif ClassType == "TextView":
        if "TextView" in source:
            List = driver.find_elements_by_class_name('android.widget.TextView')

    elif ClassType == "ImageView":
        if "ImageView" in source:
            List = driver.find_elements_by_class_name('android.widget.ImageView')

    elif ClassType == "ImageButton":
        if "ImageButton" in source:
            List = driver.find_elements_by_class_name('android.widget.ImageButton')
    for el in List:
        el.clicked = False

    print("list size for " + ClassType + " is: " + str(len(List)))

    return List


def UpdateView(driver, CurrentView):
    print("updating view")
    _buttonViewList = FindElements('ButtonView', driver)
    _editViewList = FindElements('EditView', driver)
    _textViewList = FindElements('TextView', driver)
    _imageViewList = FindElements('ImageView', driver)
    _ImageButton = FindElements('ImageButton', driver)

    CurrentView.ButtonViewList = compareEl(CurrentView.ButtonViewList, _buttonViewList)
    CurrentView.EditViewList = compareEl(CurrentView.EditViewList, _editViewList)
    CurrentView.TextViewList = compareEl(CurrentView.TextViewList, _textViewList)
    CurrentView.ImageViewList = compareEl(CurrentView.ImageViewList, _imageViewList)
    CurrentView.ImageButtonList = compareEl(CurrentView.ImageButtonList, _ImageButton)
    return CurrentView


def compareEl(oldList, NewList):
    if len(NewList) == len(oldList):
        for i, item in enumerate(oldList):
            if oldList[i] is None or oldList[i].clicked:
                NewList[i] = None
    return NewList
