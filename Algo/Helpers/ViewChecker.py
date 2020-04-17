import os

import cv2
import numpy as np
from Algo.Classes.View import View
from Algo.Helpers.Generator import TakeScreenShot
from Algo.Helpers.ImageComputing import ImageComputing
from Algo.Helpers.InformationHolder import getViewList


def ActivityChecker(OldActivity, NewActivity):
    if OldActivity == NewActivity:
        return True
    else:
        return False


# if it's not same view it returns true else returns false
def ViewChecker(img1, img2):
    res = ImageComputing(img1, img2)
    print("cmparing: " + img1 + " with " + img2 + " the score is " + str(res))
    if res >= 95:
        return False
    else:
        return True


def CheckOldViews(driver):
    ButtonView = driver.find_elements_by_class_name('android.widget.Button')
    EditView = driver.find_elements_by_class_name('android.widget.EditText')
    TextView = driver.find_elements_by_class_name('android.widget.TextView')
    ImageView = driver.find_elements_by_class_name('android.widget.ImageView')
    ImageButton = driver.find_elements_by_class_name('android.widget.ImageButton')
    CheckedTextView = driver.find_elements_by_class_name("android.widget.CheckedTextView")
    Views = getViewList()

    img2 = os.getcwd() + "/ScreenShots/temp.png"
    driver.get_screenshot_as_file(img2)

    for V in Views:
        if len(V.ImageViewList) == len(ImageView) and len(V.TextViewList) == len(TextView)  and len(V.EditViewList) == len(EditView)  and len(V.ButtonViewList) == len(ButtonView)  and len(V.ImageButtonList) == len(ImageButton) and len(V.CheckedTextList) == len(CheckedTextView):
            img1 = V.getScreenShotLocation()
            if not ViewChecker(img1, img2):
                return V
    return None
