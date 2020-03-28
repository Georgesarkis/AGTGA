import time
import cv2
import numpy as np

from Algo.Classes.View import View

TestCaseCount = 0
ActionCount = 1
Views = []
WaitTime = 0

def NewView(driver, CurrentView):
    global Views
    ActionCount = getActionCount()

    AppendToLog("new View has been created with view id: " + str(CurrentView.id + 1))
    ScreenShotLocation = "F:/AGTGA/ScreenShots/" + "V" + str(ActionCount - 1) + ".png"
    ButtonViewList = FindElements('ButtonView', driver)
    EditViewList = FindElements('EditView', driver)
    TextViewList = FindElements('TextView', driver)
    ImageViewList = FindElements('ImageView', driver)

    # Create new object for View
    ViewIDCount = CurrentView.id + 1
    CurrentView = View(ViewIDCount, ScreenShotLocation, ImageViewList, TextViewList, EditViewList, ButtonViewList)
    Views.append(CurrentView)
    print("Views list size: " + str(len(Views)))


def ClickButton(driver, el):
    global WaitTime
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


def ActivityChecker(OldActivity, NewActivity):
    if(OldActivity == NewActivity):
        return True
    else:
        return False


def ViewChecker(img1, img2):
    image1 = cv2.imread(img1)
    image2 = cv2.imread(img2)
    return not (image1.shape == image2.shape and not (np.bitwise_xor(image1, image2).any()))


def FindElements(ClassType, driver):
    source = driver.page_source

    List = []
    if (ClassType == "ButtonView"):
        if "Button" in source:
            List = driver.find_elements_by_class_name('android.widget.Button')

    elif (ClassType == "EditView"):
        if "EditText" in source:
            List = driver.find_elements_by_class_name('android.widget.EditText')

    elif (ClassType == "TextView"):
        if "TextView" in source:
            List = driver.find_elements_by_class_name('android.widget.TextView')

    elif (ClassType == "ImageView"):
        if "ImageView" in source:
            List = driver.find_elements_by_class_name('android.widget.ImageView')
    for el in List:
        el.clicked = False

    print("list size for " + ClassType + " is: " + str(len(List)))

    return List


def AppendToLog(log):
    global TestCaseCount

    log = log + "\n"
    print(log)
    file1 = open("F:/AGTGA/ScreenShots/log" + str(TestCaseCount) + ".txt", "a")
    file1.write(log)
    file1.close()


def TakeScreenShot(t, driver):
    global ActionCount
    time.sleep(t)
    ScreenShotLocation = "F:/AGTGA/ScreenShots/" + "V" + str(ActionCount) + ".png"
    ActionCount = ActionCount + 1
    driver.get_screenshot_as_file(ScreenShotLocation)
    return ScreenShotLocation


def getActionCount():
    global ActionCount
    return ActionCount


def getViewList():
    global Views
    return Views


def setWaitTime(time):
    global WaitTime
    WaitTime = time
