from Algo.Helpers.Handler import FindElements, ClickButton, NewView
from Algo.Helpers.ViewChecker import CheckOldViews
import random
import string

from Algo.Helpers.InformationHolder import getViewList, getViewElementPairs, setRootView, setViewElementPair


def ActionCoverageAlgo(_driver, _currentView):
    setRootView(_currentView)
    MainActionCoverageAlgo(_driver, _currentView)

def MainActionCoverageAlgo(_driver, _currentView):
    print("ActionCoverageAlgo")
    _currentView = RecursiveActionCoverage(_driver, _currentView)
    print("All actions has been excecuted from this View, Trying to find unexcecuted actions...")
    _desiredView = FindUnexecutedElements()
    if _desiredView is not None:
        pairList = FindShortestDistanceToView(_driver, _currentView, _desiredView)
        print("Reach to View and run the ActionCoverageAlgo()")
        if pairList is None:
            print("COULD NOT PERFORM FULL TESTING, NUMBER OF ACTIONS PERFORMED .... and NUMBER OF ELEMENTS SKEPT....")
        else:
            print("found the shortest distance, taking proper actions")
            ActionsToDesiredView(pairList)
            MainActionCoverageAlgo(_driver, pairList[len(pairList) - 1].ChildView)
    else:
        print("EVERYTHING IS DONE; YOU ARE AMAZING")


def RecursiveActionCoverage(_driver, _currentView):
    el = ChooseElement(_currentView)
    view = _currentView
    if el is not None:
        if ClickButton(_driver, el):
            res = CheckOldViews(_driver)
            if res is not None:
                print("found old view with id: " + str(res.SelfID))
                view = res
            else:
                NewView(_driver, view)
            setViewElementPair(_currentView, el, view)
            return RecursiveActionCoverage(_driver, view)
        else:
            return RecursiveActionCoverage(_driver, view)
    else:
        return view


def ChooseElement(_currentView):
    ButtonListView = _currentView.ButtonViewList
    TextViewList = _currentView.TextViewList
    ImageViewList = _currentView.ImageViewList

    for el in ButtonListView:
        if el.clicked == False:
            return el
    for el in ImageViewList:
        if el.clicked == False:
            return el
    for el in TextViewList:
        if el.clicked == False:
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


def ActionsToDesiredView(pairList):
    for pair in pairList:
        ClickButton(pair.Element)


def FindUnexecutedElements():
    _viewList = getViewList()

    for view in _viewList:
        for el in view.ImageViewList:
            if el.clicked is False:
                return view
        for el in view.TextViewList:
            if el.clicked is False:
                return view
        for el in view.ButtonViewList:
            if el.clicked is False:
                return view
    return None


def FindShortestDistanceToView(_driver, _currentView, _desieredView):
    if FindShortestDistanceToViewRecursive(_currentView, _desieredView) is None:
        _driver.back()
        return FindShortestDistanceToViewRecursive(_currentView, _desieredView)


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
