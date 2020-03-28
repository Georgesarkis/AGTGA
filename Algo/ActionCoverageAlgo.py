from Algo.Helpers.ViewChecker import FindElements, ClickButton
import random
import string
driver = None
CurrentView = None

def ActionCoverageAlgo(_driver,_currentView):
    global driver, CurrentView
    driver = _driver
    CurrentView = _currentView

    el = ChooseElement(_currentView)

    while (el is not None):
        ClickButton(_driver, el)


    print("ActionCoverageAlgo")


def ChooseElement(_currentView):
    ButtonListView = CurrentView.ButtonViewList
    TextViewList = CurrentView.TextViewList
    ImageViewList = CurrentView.ImageViewList

    for el in ButtonListView:
        if el.Clicked == False:
            return el
    for el in TextViewList:
        if el.Clicked == False:
            return el
    for el in ImageViewList:
        if el.Clicked == False:
            return el
    return None

def FillEditView(_driver, _currentView):
    ## TODO: take screenshot here, before filling in editView
    EditViewList = _currentView.EditViewList
    for el in EditViewList:
        el.clicked = True
        el.click()
        el.send_keys(randomString())
        _driver.back()
    ## TODO: take screenshot here, after filling in editView
    ## TODO: compore both screenshots to know if something big has been change


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))