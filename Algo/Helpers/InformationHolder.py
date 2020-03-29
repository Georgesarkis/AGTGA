from Algo.Classes.ViewElementPair import ViewElementPair

TestCaseCount = 0
ActionCount = 0
Views = []
WaitTime = 0
ViewElementPairs = []
RootView = None
count = 0
desired_caps = None
port = None
algo = ""
username = ""
password = ""
durationToWait = 0
TestServer = False


def getPort():
    global port
    return port


def setPort(p):
    global port
    port = p


def getDesiredCap():
    global desired_caps
    return desired_caps


def setDesiredCap(d):
    global desired_caps
    desired_caps = d


def getAlgo():
    global algo
    return algo


def setAlgo(a):
    global algo
    algo = a


def getUsername():
    global username
    return username


def setUsername(u):
    global username
    username = u


def getPassord():
    global password
    return password

def setPassword(p):
    global password
    password = p

def getDurationToWait():
    global durationToWait
    return durationToWait


def setDurationToWait(t):
    global durationToWait
    durationToWait = t



def getTestServer():
    global TestServer
    return TestServer


def setTestServer(t):
    global TestServer
    TestServer = t



def getCount():
    global count
    return count


def setCount(c):
    global count
    count = c


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
