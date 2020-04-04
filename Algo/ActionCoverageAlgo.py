import time
from appium import webdriver
from random import *
from Algo.Helpers.Generator import AppendCodeClickButton
from Algo.Helpers.Handler import FindElements, ClickButton, NewView, UpdateView, ClickBackButton
from Algo.Helpers.ViewChecker import CheckOldViews
import random
import string

from Algo.Helpers.InformationHolder import *


def ActionCoverageAlgo(_driver, _currentView):
    return MainActionCoverageAlgo(_driver, _currentView)


def MainActionCoverageAlgo(_driver, _v):
    print("ActionCoverageAlgo")
    _currentView = RecursiveActionCoverage(_driver, _v)
    if _v.SelfID == _currentView.SelfID:
        print("could not found any more execution!")
        return True
    print("will press back button")
    ClickBackButton(_driver)
    BackView = CheckOldViews(_driver)
    print("COULD NOT PERFORM FULL TESTING, NUMBER OF ACTIONS PERFORMED " + str(
        getActionCount()) + " trying to go back and try again")
    if BackView is not None:
        return MainActionCoverageAlgo(_driver, BackView)
    else:
        Currentactivity = _driver.current_activity
        if Currentactivity[:2] == getActivity()[:2]:
            print("New view has been found...")
            View = NewView(_driver, _currentView)
            return MainActionCoverageAlgo(_driver, View)
        else:
            print("Close the app unintentionally, will try to start again")
            return False


def RecursiveActionCoverage(_driver, _currentView):
    el = ChooseElement(_currentView, False, False, False, False)
    view = _currentView
    if el is not None:
        if ClickButton(_driver, el):
            res = CheckOldViews(_driver)
            if res is not None:
                print("found old view with id: " + str(res.SelfID))
                print("old view screenshot location is :" + res.ScreenShotLocation)
                view = UpdateView(_driver, res)
            else:
                view = NewView(_driver, view)
            return RecursiveActionCoverage(_driver, view)
        else:
            return RecursiveActionCoverage(_driver, view)
    else:
        return view


def ChooseElement(_currentView, ButtonListViewChecked, ImageViewListChecked, TextViewListChecked,
                  ImageButtonListChecked):
    ButtonListView = _currentView.ButtonViewList
    TextViewList = _currentView.TextViewList
    ImageViewList = _currentView.ImageViewList
    ImageButtonList = _currentView.ImageButtonList

    RandomList = random.randrange(1, 5)

    if not ButtonListViewChecked and RandomList == 1:
        for el in ButtonListView:
            if el is not None and el.clicked is False:
                el = randomElementSelector(ButtonListView, 0)
                if el is not None:
                    return el
        ButtonListViewChecked = True
        return ChooseElement(_currentView, ButtonListViewChecked, ImageViewListChecked, TextViewListChecked, ImageButtonListChecked)

    if not ImageViewListChecked and RandomList == 2:
        for el in ImageViewList:
            if el is not None and el.clicked is False:
                el = randomElementSelector(ImageViewList, 0)
                if el is not None:
                    return el
        ImageViewListChecked = True
        return ChooseElement(_currentView, ButtonListViewChecked, ImageViewListChecked, TextViewListChecked, ImageButtonListChecked)

    if not TextViewListChecked and RandomList == 3:
        for el in TextViewList:
            if el is not None and el.clicked is False:
                el = randomElementSelector(TextViewList, 0)
                if el is not None:
                    return el
        TextViewListChecked = True
        return ChooseElement(_currentView, ButtonListViewChecked, ImageViewListChecked, TextViewListChecked, ImageButtonListChecked)

    if not ImageButtonListChecked and RandomList == 4:
        for el in ImageButtonList:
            if el is not None and el.clicked is False:
                el = randomElementSelector(ImageButtonList, 0)
                if el is not None:
                    return el
        ImageButtonListChecked = True
        return ChooseElement(_currentView, ButtonListViewChecked, ImageViewListChecked, TextViewListChecked, ImageButtonListChecked)

    if TextViewListChecked and ImageViewListChecked and ButtonListViewChecked and ImageButtonListChecked:
        return None
    else:
        return ChooseElement(_currentView, ButtonListViewChecked, ImageViewListChecked, TextViewListChecked,ImageButtonListChecked)


def randomElementSelector(list, count):
    ListSize = len(list)
    i = random.randrange(0, ListSize)
    if count >= len(list):
        return None
    if list[i] is not None and list[i].clicked is False:
        return list[i]
    else:
        return randomElementSelector(list, count + 1)


def FillEditView(_driver, _currentView):
    ## TODO: take screenshot here, before filling in editView
    EditViewList = _currentView.EditViewList
    for el in EditViewList:
        el.clicked = True
        AppendCodeClickButton(el)
        el.click()
        el.send_keys(randomString())
        ClickBackButton(_driver)
    ## TODO: take screenshot here, after filling in editView
    ## TODO: compore both screenshots to know if something big has been change


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
