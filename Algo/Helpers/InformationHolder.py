from Algo.Classes.ViewElementPair import ViewElementPair

TestCaseCount = 0
ActionCount = 1
Views = []
WaitTime = 0
ViewElementPairs = []
RootView = None


def getTestCaseCount():
    global TestCaseCount
    return TestCaseCount


def getActionCount():
    global ActionCount
    return ActionCount


def getViewList():
    global Views
    return Views


def setWaitTime(time):
    global WaitTime
    WaitTime = time


def getWaitTime():
    global WaitTime
    return WaitTime


def getRootView():
    global RootView
    return RootView


def setRootView(_rootView):
    global RootView
    RootView = _rootView


def getViewElementPairs():
    global ViewElementPairs
    return ViewElementPairs


def setViewElementPair(ParentView, Element, ChildView):
    global ViewElementPairs
    _viewElementPair = ViewElementPair(ParentView, Element, ChildView)
    ViewElementPairs.append(_viewElementPair)


def setActionCount(_actionCount):
    global ActionCount
    ActionCount = _actionCount
