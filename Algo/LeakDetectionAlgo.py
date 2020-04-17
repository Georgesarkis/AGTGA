import os

from Algo.Helpers.Generator import *
from Algo.Helpers.Generator import *
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
            AppendCodeLeakDetectionRotation()
        except:
            AppendToLog("The application does not allow rotation")
            setPossibleToRotate(False)
            AppendCodeLeakDetectionRotation()
            return False

    if getPossibleToGoBackground():
        oldScreenShot = os.getcwd() + "/ScreenShots/oldScreenShot.png"
        driver.get_screenshot_as_file(oldScreenShot)
        oldActvity = driver.current_activity
        print("setting application to the background")
        driver.background_app(1)
        time.sleep(10)
        newActivity = driver.current_activity
        newScreenshot = os.getcwd() + "/ScreenShots/newScreenshot.png"
        driver.get_screenshot_as_file(newScreenshot)
        if oldActvity is newActivity:
            if ViewChecker(newScreenshot, oldScreenShot):
                setPossibleToGoBackground(True)
                AppendCodeLeakDetectionBackground()
            else:
                setPossibleToGoBackground(False)
                AppendCodeLeakDetectionBackground()
                return False
        else:
            setPossibleToGoBackground(False)
            AppendCodeLeakDetectionBackground()
            return False

    return True
