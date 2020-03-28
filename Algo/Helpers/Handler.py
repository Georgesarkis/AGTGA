import time

from Algo.Classes.View import View
from Algo.Helpers.Generator import AppendToLog, TakeScreenShot
from Algo.Helpers.InformationHolder import getActionCount, getViewList, getWaitTime
from Algo.Helpers.ViewChecker import ActivityChecker, ViewChecker


def NewView(driver, CurrentView):
    Views = getViewList()
    ActionCount = getActionCount()

    AppendToLog("new View has been created with view id: " + str(CurrentView.SelfID + 1))
    ScreenShotLocation = "F:/AGTGA/ScreenShots/" + "V" + str(ActionCount - 1) + ".png"
    ButtonViewList = FindElements('ButtonView', driver)
    EditViewList = FindElements('EditView', driver)
    TextViewList = FindElements('TextView', driver)
    ImageViewList = FindElements('ImageView', driver)

    # Create new object for View
    ViewIDCount = CurrentView.SelfID + 1
    CurrentView = View(ViewIDCount, ScreenShotLocation, ImageViewList, TextViewList, EditViewList, ButtonViewList)
    Views.append(CurrentView)
    print("Views list size: " + str(len(Views)))
    return CurrentView


def ClickButton(driver, el):
    WaitTime = getWaitTime()
    AppendToLog("button with id: " + str(el.id) + " with string value: " + el.text + " has been clicked")
    oldActivity = driver.current_activity
    el.clicked = True
    el.click()
    time.sleep(WaitTime)
    TakeScreenShot(0, driver)
    if ActivityChecker(oldActivity, driver.current_activity):
        ActionCount = getActionCount()
        ScreenShotLocation1 = "F:/AGTGA/ScreenShots/" + "V" + str(ActionCount - 2) + ".png"
        ScreenShotLocation2 = "F:/AGTGA/ScreenShots/" + "V" + str(ActionCount - 1) + ".png"
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
    for el in List:
        el.clicked = False

    print("list size for " + ClassType + " is: " + str(len(List)))

    return List
