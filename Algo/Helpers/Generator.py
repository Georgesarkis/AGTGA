import os
import time
from Algo.Helpers.InformationHolder import  getActionCount, setActionCount,getCount


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

