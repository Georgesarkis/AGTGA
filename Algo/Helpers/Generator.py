import time
from Algo.Helpers.InformationHolder import getTestCaseCount, getActionCount, setActionCount


def AppendToLog(log):
    print(log)
    log = log + "\n"
    file1 = open("F:/AGTGA/ScreenShots/log" + str(getTestCaseCount()) + ".txt", "a")
    file1.write(log)
    file1.close()


def TakeScreenShot(t, driver):
    _actionCount = getActionCount()
    time.sleep(t)
    ScreenShotLocation = "F:/AGTGA/ScreenShots/" + "V" + str(_actionCount) + ".png"
    setActionCount(_actionCount + 1)
    driver.get_screenshot_as_file(ScreenShotLocation)
    return ScreenShotLocation

