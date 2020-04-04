import os

from Algo.Helpers.Generator import AppendToLog, AppendCodeLeakDetection
from Algo.Helpers.InformationHolder import *
from Algo.Helpers.ViewChecker import ViewChecker


def LeakDetectionAlgo(driver):
    print("LeakDetectionAlgo")
    if getPossibleToRotate():
        try:
            AppendToLog("rotating the screen to LANDSCAPE")
            driver.orientation = "LANDSCAPE"
            AppendToLog("rotating the screen to PORTRAIT")
            driver.orientation = "PORTRAIT"
            AppendToLog("setting the app to the background")
        except:
            AppendToLog("The application does not allow rotation")
            setPossibleToRotate(False)

    if getPossibleToGoBackground():
        oldScreenShot = os.getcwd() + "/ScreenShots/oldScreenShot.png"
        driver.get_screenshot_as_file(oldScreenShot)
        oldActvity = driver.current_activity
        print("setting application to the background")
        driver.background_app(1)
        newActivity = driver.current_activity
        newScreenshot = os.getcwd() + "/ScreenShots/newScreenshot.png"
        driver.get_screenshot_as_file(newScreenshot)
        if oldActvity is newActivity:
            if ViewChecker(newScreenshot, oldScreenShot):
                setPossibleToGoBackground(False)
        else:
            setPossibleToGoBackground(False)

    AppendCodeLeakDetection(getPossibleToGoBackground(), getPossibleToRotate())