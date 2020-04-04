from Algo.Helpers.Generator import AppendToLog, AppendCodeLeakDetection


def LeakDetectionAlgo(driver):
    try:
        AppendToLog("rotating the screen to LANDSCAPE")
        driver.orientation = "LANDSCAPE"
        AppendToLog("rotating the screen to PORTRAIT")
        driver.orientation = "PORTRAIT"
        AppendToLog("setting the app to the background")
    except:
        AppendToLog("The application does not allow rotation")

    driver.background_app(10)
    AppendCodeLeakDetection()