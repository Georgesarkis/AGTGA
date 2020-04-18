import os
import time

from Algo.Classes.View import View
from Algo.Helpers.Generator import AppendToLog, TakeScreenShot, AppendCodeClickButton, AppendCodeBackButtonClick, \
    AppendCodeEditText
from Algo.Helpers.InformationHolder import *
from Algo.Helpers.ViewChecker import ActivityChecker, ViewChecker
from Algo.LeakDetectionAlgo import LeakDetectionAlgo


def NewView(driver, CurrentView):
    AddNumberOfViewsInThisTestCase()
    Views = getViewList()
    ActionCount = getActionCount()
    TestCaseCount = str(getCount())

    path = os.getcwd() + "/ScreenShots/" + TestCaseCount
    if not os.path.exists(path):
        os.makedirs(path)
    AppendToLog("new View has been created with view id: " + str(CurrentView.SelfID + 1))
    ScreenShotLocation = path + "/V" + str(ActionCount - 1) + ".png"
    ButtonViewList = FindElements('ButtonView', driver)
    EditViewList = FindElements('EditView', driver)
    TextViewList = FindElements('TextView', driver)
    ImageViewList = FindElements('ImageView', driver)
    ImageButtonList = FindElements("ImageButton", driver)
    CheckedTextList = FindElements("CheckedTextView", driver)

    # Create new object for View
    ViewIDCount = CurrentView.SelfID + 1
    CurrentView = View(ViewIDCount, ScreenShotLocation, ImageViewList, TextViewList, EditViewList, ButtonViewList, ImageButtonList, CheckedTextList)
    print("new view is created with screenshot location: " + ScreenShotLocation)
    Views.append(CurrentView)
    if getVerbose(): print("Views list size: " + str(len(Views)))

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
        ScreenShotLocation1 = os.getcwd() + "/ScreenShots/" + str(getCount()) + "/V" + str(ActionCount - 2) + ".png"
        ScreenShotLocation2 = os.getcwd() + "/ScreenShots/" + str(getCount()) + "/V" + str(ActionCount - 1) + ".png"
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

    elif ClassType == "CheckedTextView":
        if "CheckedTextView" in source:
            List = driver.find_elements_by_class_name("android.widget.CheckedTextView")

    for el in List:
        el.clicked = False
    if getVerbose(): print("list size for " + ClassType + " is: " + str(len(List)))

    return List


def UpdateView(driver, CurrentView):
    if getVerbose(): print("updating view")
    _buttonViewList = FindElements('ButtonView', driver)
    _editViewList = FindElements('EditView', driver)
    _textViewList = FindElements('TextView', driver)
    _imageViewList = FindElements('ImageView', driver)
    _ImageButton = FindElements('ImageButton', driver)
    _checkedTextList = FindElements("CheckedTextView", driver)

    CurrentView.ButtonViewList = compareEl(CurrentView.ButtonViewList, _buttonViewList)
    CurrentView.EditViewList = compareEl(CurrentView.EditViewList, _editViewList)
    CurrentView.TextViewList = compareEl(CurrentView.TextViewList, _textViewList)
    CurrentView.ImageViewList = compareEl(CurrentView.ImageViewList, _imageViewList)
    CurrentView.ImageButtonList = compareEl(CurrentView.ImageButtonList, _ImageButton)
    CurrentView.CheckedTextList = compareEl(CurrentView.CheckedTextList, _checkedTextList)

    return CurrentView


def compareEl(oldList, NewList):
    if len(NewList) == len(oldList):
        for i, item in enumerate(oldList):
            if oldList[i] is None or oldList[i].clicked:
                NewList[i] = None
    return NewList


def FillEditView(driver,editViewList, userName, password):
    if len(editViewList) == 2:
        username = editViewList[0]
        AppendToLog("EditView with id: " + str(username.id) + " has been clicked and filled with string: " + userName)
        username.clicked = True
        username.click()
        username.send_keys(userName)
        AppendCodeEditText(username, userName)
        Password = editViewList[1]
        AppendToLog("EditView with id: " + str(username.id) + " has been clicked and filled with string: " + password)
        Password.clicked = True
        Password.click()
        Password.send_keys(password)
        AppendCodeEditText(Password, password)
        ClickBackButton(driver)


def ClickLoginButton(driver, ButtonViewList=None, TextViewList=None):
    if ButtonViewList is None:
        ButtonViewList = driver.find_elements_by_class_name('android.widget.Button')
    if TextViewList is None:
        TextViewList = driver.find_elements_by_class_name('android.widget.TextView')

    for el in ButtonViewList:
        if el.text.lower() == "login" or el.text.lower() == "signin" or el.text.lower() == "log in" or el.text.lower() == "sign in" or el.text.lower() == "logga in":
            if getVerbose(): print("in login button if statment")
            return ClickButton(driver, el)
    for el in TextViewList:
        if el.text.lower() == "login" or el.text.lower() == "signin" or el.text.lower() == "log in" or el.text.lower() == "sign in" or el.text.lower() == "logga in":
            if getVerbose(): print("in login button if statment")
            return ClickButton(driver, el)
