import time
from appium import webdriver
from random import *
from Algo.Helpers.Generator import AppendCodeClickButton
from Algo.Helpers.Handler import FindElements, ClickButton, NewView, UpdateView, ClickButtonXY, ClickBackButton
from Algo.Helpers.ViewChecker import CheckOldViews
import random
import string

from Algo.Helpers.InformationHolder import *
from Algo.LeakDetectionAlgo import LeakDetectionAlgo
from Algo.StateCoverageAlgo import StateCoverageAlgo


def ActionCoverageAlgo(_driver, _currentView):
    setRootView(_currentView)
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
        return MainActionCoverageAlgo(_driver, BackView)  ###restartTheDriver(_driver)
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
            setViewElementPair(_currentView, el, view)
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
                return randomElementSelector(ButtonListView, 0)
        ButtonListViewChecked = True
        return ChooseElement(_currentView, ButtonListViewChecked, ImageViewListChecked, TextViewListChecked)

    if not ImageViewListChecked and RandomList == 2:
        for el in ImageViewList:
            if el is not None and el.clicked is False:
                return randomElementSelector(ImageViewList, 0)
        ImageViewListChecked = True
        return ChooseElement(_currentView, ButtonListViewChecked, ImageViewListChecked, TextViewListChecked)

    if not TextViewListChecked and RandomList == 3:
        for el in TextViewList:
            if el is not None and el.clicked is False:
                return randomElementSelector(TextViewList, 0)
        TextViewListChecked = True
        return ChooseElement(_currentView, ButtonListViewChecked, ImageViewListChecked, TextViewListChecked)

    if not ImageButtonListChecked and RandomList == 4:
        for el in ImageButtonList:
            if el is not None and el.clicked is False:
                return randomElementSelector(TextViewList, 0)
        ImageButtonListChecked = True
        return ChooseElement(_currentView, ButtonListViewChecked, ImageViewListChecked, ImageButtonListChecked)

    if TextViewListChecked and ImageViewListChecked and ButtonListViewChecked and ImageButtonListChecked:
        return None
    else:
        return ChooseElement(_currentView, ButtonListViewChecked, ImageViewListChecked, TextViewListChecked,
                             ImageButtonListChecked)


def randomElementSelector(list, count):
    ListSize = len(list)
    choice = random.randrange(0, ListSize)
    if count >= len(list):
        return None
    if list[choice] is not None and list[choice].clicked is False:
        return list[choice]
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


def ActionsToDesiredView(_driver, pairList):
    for pair in pairList:
        ClickButtonXY(_driver, pair.Element)  ##TODO THIS NEEDS TO BE CHANGED


def FindUnexecutedElements():
    _viewList = getViewList()

    for view in _viewList:
        for el in view.ImageViewList:
            if el is not None and el.clicked is False:
                return view
        for el in view.TextViewList:
            if el is not None and el.clicked is False:
                return view
        for el in view.ButtonViewList:
            if el is not None and el.clicked is False:
                return view
    return None


def FindShortestDistanceToView(_driver, _currentView, _desieredView):
    path = FindShortestDistanceToViewRecursive(_currentView, _desieredView)
    return path


def FindShortestDistanceToViewRecursive(_currentView, _desieredView):
    ElementViewPair = getViewElementPairs()
    for pair in ElementViewPair:
        if pair.ParentView == pair.ChildView:
            return [pair]
    for pair in ElementViewPair:
        if pair.ParentView == _currentView:
            chainPair = pair
            for pair2 in ElementViewPair:
                if chainPair is not pair and chainPair.ChildView == _desieredView:
                    return [chainPair, pair2]
            for pair2 in ElementViewPair:
                if pair2.ChildView == _desieredView:
                    for pair3 in ElementViewPair:
                        if pair3.ChildView == pair2.Parent and pair2.parrent == pair.ChildView:
                            return [pair, pair2, pair3]
    return None


def AlgoMain(_driver, _currentView, algo, username, password, durationToWait, TestServer):
    CurrentView = _currentView
    Views = getViewList()
    Views.append(CurrentView)
    driver = _driver
    setWaitTime(durationToWait)

    if username != "" and password != "":
        FillEditView(CurrentView.getEditViewList(), username, password)
        print("will press back button")
        ClickBackButton(driver)

        if ClickLoginButton(driver, CurrentView.getButtonViewList()) and TestServer:
            if ConnectToTestServer(driver):
                time.sleep(10)
                CurrentView = NewView(driver, CurrentView)
            else:
                print("something bad happend when trying to connect to test server")
                time.sleep(10)
                CurrentView = NewView(driver, CurrentView)
        else:
            time.sleep(10)
            CurrentView = NewView(driver, CurrentView)
    else:
        time.sleep(10)
        CurrentView = NewView(driver, CurrentView)

    if algo == "StateCoverage":
        StateCoverageAlgo()

    elif algo == "ActionCoverage":
        ActionCoverageAlgo(driver, CurrentView)

    elif algo == "LeakDetection":
        LeakDetectionAlgo()


def restartTheDriver(driver):
    driver.quit()
    count = getCount()
    driver = webdriver.Remote(command_executor=getPort(), desired_capabilities=getDesiredCap())
    CurrentView = NewView()
    print("run number: " + str(count))
    setCount(count + 1)
    Finished = AlgoMain(driver, CurrentView, getAlgo(), getUsername(), getPassord(), getDurationToWait(),
                        getTestServer())
    return Finished


def ClickLoginButton(driver, ButtonViewList):
    for el in ButtonViewList:
        if el.text.lower() == "login" or el.text.lower() == "signin" or el.text.lower() == "log in" or el.text.lower() == "sign in":
            return ClickButton(driver, el)


def ConnectToTestServer(driver):
    ButtonViewList = FindElements('ButtonView', driver)
    for el in ButtonViewList:
        if el.text.lower() == "yes":
            return ClickButton(driver, el)
    return False
