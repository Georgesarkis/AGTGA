from appium import webdriver
from Algo.Algo import AlgoMain
from Algo.Classes.View import View
from Algo.Helpers.Handler import FindElements
from Algo.Helpers.InformationHolder import getTestCaseCount

driver = None
TestCaseCount = 0


def run(desired_caps, username, password, algo, durationToWait, TestServer):
    port = 'http://localhost:4723/wd/hub'
    global driver
    _testCaseCount = getTestCaseCount()
    banana = True
    count = 0

    while banana:
        try:
            driver = webdriver.Remote(command_executor=port, desired_capabilities=desired_caps)
            CurrentView = NewView()
            print("run number: " + str(count))
            AlgoMain(driver, CurrentView, algo, username, password, durationToWait, _testCaseCount, TestServer)

            driver.quit()
        except Exception as e:
            print("Exception aquired with message: " + str(e))
            count = count + 1
            print("do you want to stop?")
            input1 = input()
            banana = not (input1 == "y")


def NewView():
    # CreateLog
    ScreenShotLocation = CreateTheLog(driver)

    # Create new object from every single element group
    ButtonViewList = FindElements("ButtonView", driver)
    EditViewList = FindElements("EditView", driver)
    TextViewList = FindElements("TextView", driver)
    ImageViewList = FindElements("ImageView", driver)

    # Create new object for View
    ViewIDCount = 0
    return View(ViewIDCount, ScreenShotLocation, ImageViewList, TextViewList, EditViewList, ButtonViewList)


def CreateTheLog(driver):
    log = "New View Has been Created, The activity name is " + driver.current_activity +"\n"
    _testCaseCount = getTestCaseCount()
    file1 = open("F:/AGTGA/ScreenShots/log" + str(_testCaseCount) + ".txt", "w+")
    _testCaseCount = _testCaseCount + 1
    file1.write(log)
    file1.close()
    ViewIDCount = 0
    ScreenShotLocation = "F:/AGTGA/ScreenShots/" + "V" + str(ViewIDCount) + ".png"
    driver.get_screenshot_as_file(ScreenShotLocation)
    return ScreenShotLocation
