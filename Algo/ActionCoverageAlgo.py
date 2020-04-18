import time
from appium import webdriver
from random import *
from Algo.Helpers.Generator import AppendCodeClickButton, AppendCodeEditText
from Algo.Helpers.Handler import *
from Algo.Helpers.ViewChecker import CheckOldViews
from Algo.Helpers.InformationHolder import *
import random
import string



def ActionCoverageAlgo(_driver, _currentView):
    return MainActionCoverageAlgo(_driver, _currentView)


def MainActionCoverageAlgo(_driver, _v):
    if getVerbose(): print("ActionCoverageAlgo")
    _currentView = RecursiveActionCoverage(_driver, _v)

    if _currentView == None:
        if getVerbose(): print("restarting the AGTGA")
        return False

    """
    elif _v.SelfID == _currentView.SelfID:
        print("could not found any more execution!")
        return True
    """

    if getVerbose(): print("will press back button")
    ClickBackButton(_driver)
    BackView = CheckOldViews(_driver)
    if getVerbose(): print("COULD NOT PERFORM FULL TESTING, NUMBER OF ACTIONS PERFORMED " + str(getActionCount()) + " trying to go back and try again")
    if BackView is not None:
        return MainActionCoverageAlgo(_driver, BackView)
    else:
        Currentactivity = _driver.current_activity
        if Currentactivity[:2] == getActivity()[:2]:
            if getVerbose(): print("New view has been found...")
            View = NewView(_driver, _currentView)
            return MainActionCoverageAlgo(_driver, View)
        else:
            if getVerbose(): print("Close the app unintentionally, will try to start again")
            return False


def ApplicationCrashed(_currentView):
    if len(_currentView.TextViewList) == 1 and "has stopped" in _currentView.TextViewList[0].text:
        return True
    return False


def RecursiveActionCoverage(_driver, _currentView):
    if ApplicationCrashed(_currentView):
        return None

    FillEditFiled(_driver, _currentView)
    el = ChooseElement(_currentView, False, False, False, False, False)
    view = _currentView
    if el is not None:
        if ClickButton(_driver, el):
            res = CheckOldViews(_driver)
            if res is not None:
                if getVerbose(): print("found old view with id: " + str(res.SelfID))
                if getVerbose(): print("old view screenshot location is :" + res.ScreenShotLocation)
                view = UpdateView(_driver, res)
                if view.getSelfID() == GetRootView().getSelfID():
                    return None

            else:
                view = NewView(_driver, view)
                if getLeakDetection() and (getPossibleToRotate() or getPossibleToGoBackground()):
                    if not LeakDetectionAlgo(_driver):
                        return None

            return RecursiveActionCoverage(_driver, view)
        else:
            return RecursiveActionCoverage(_driver, view)
    else:
        return view


def ChooseElement(_currentView, ButtonListViewChecked, ImageViewListChecked, TextViewListChecked, ImageButtonListChecked, CheckTextListChecked):
    ButtonListView = _currentView.ButtonViewList
    TextViewList = _currentView.TextViewList
    ImageViewList = _currentView.ImageViewList
    ImageButtonList = _currentView.ImageButtonList
    CheckTextList = _currentView.CheckedTextList
    RandomList = random.randrange(1, 6)

    if not ButtonListViewChecked and RandomList == 1:
        for el in ButtonListView:
            if el is not None and el.clicked is False:
                el = randomElementSelector(ButtonListView)
                if el is not None:
                    return el
        ButtonListViewChecked = True
        return ChooseElement(_currentView, ButtonListViewChecked, ImageViewListChecked, TextViewListChecked, ImageButtonListChecked, CheckTextListChecked)

    if not ImageViewListChecked and RandomList == 2:
        for el in ImageViewList:
            if el is not None and el.clicked is False:
                el = randomElementSelector(ImageViewList)
                if el is not None:
                    return el
        ImageViewListChecked = True
        return ChooseElement(_currentView, ButtonListViewChecked, ImageViewListChecked, TextViewListChecked, ImageButtonListChecked, CheckTextListChecked)

    if not TextViewListChecked and RandomList == 3:
        for el in TextViewList:
            if el is not None and el.clicked is False:
                el = randomElementSelector(TextViewList)
                if el is not None:
                    return el
        TextViewListChecked = True
        return ChooseElement(_currentView, ButtonListViewChecked, ImageViewListChecked, TextViewListChecked, ImageButtonListChecked, CheckTextListChecked)

    if not ImageButtonListChecked and RandomList == 4:
        for el in ImageButtonList:
            if el is not None and el.clicked is False:
                el = randomElementSelector(ImageButtonList)
                if el is not None:
                    return el
        ImageButtonListChecked = True
        return ChooseElement(_currentView, ButtonListViewChecked, ImageViewListChecked, TextViewListChecked, ImageButtonListChecked, CheckTextListChecked)

    if not CheckTextListChecked and RandomList == 5:
        for el in CheckTextList:
            if el is not None and el.clicked is False:
                el = randomElementSelector(CheckTextList)
                if el is not None:
                    return el
        CheckTextListChecked = True
        return ChooseElement(_currentView, ButtonListViewChecked, ImageViewListChecked, TextViewListChecked, ImageButtonListChecked, CheckTextListChecked)

    if TextViewListChecked and ImageViewListChecked and ButtonListViewChecked and ImageButtonListChecked and CheckTextListChecked:
        return None
    else:
        return ChooseElement(_currentView, ButtonListViewChecked, ImageViewListChecked, TextViewListChecked,ImageButtonListChecked, CheckTextListChecked)


def randomElementSelector(l):
    i = random.randrange(0, len(l))
    if l[i] is not None and l[i].clicked is False:
        return l[i]
    else:
        NewL = l.pop(i)
        return randomElementSelector(NewL)


def FillEditFiled(_driver, _currentView):
    ## TODO: take screenshot here, before filling in editView
    EditViewList = _currentView.EditViewList
    if EditViewList == 2:
        FillEditView(_driver,EditViewList, GetUsername(), GetPassword())
        ClickLoginButton(_driver, _currentView.ButtonViewList, _currentView.TextViewList)
    else:
        for el in EditViewList:
            if el.clicked == False:
                el.clicked = True
                str = randomString()
                AppendCodeEditText(el, str)
                el.click()
                el.send_keys(str)
                ClickBackButton(_driver)
    ## TODO: take screenshot here, after filling in editView
    ## TODO: compore both screenshots to know if something big has been change


def randomString():
    """Generate a random string"""
    RandomStringLength = random.randrange(1, 1000)
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(RandomStringLength))
