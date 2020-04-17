##TODO: THIS SHOULD BE CHANGE INTO CLASSES

ActionCount = 0
Views = []
WaitTime = 0
count = 0
desired_caps = None
Activity = ""
LeakDetection = False
PossibleToRotate = True
PossibleToGoBackground = True
NumberOfActionsInThisTestCase = 0
NumberOfViewsInThisTestCase = 0
LenghtOfTestCase = 0
username = ""
password = ""
RootView = None

def SetRootView(v):
    global RootView
    RootView = v

def GetRootView():
    global RootView
    return RootView

def SetUsername(u):
    global username
    username = u

def SetPassword(p):
    global password
    password = p

def GetUsername():
    global username
    return username

def GetPassword():
    global password
    return password

def RestartNumberOfActionsInThisTestCase():
    global NumberOfActionsInThisTestCase
    NumberOfActionsInThisTestCase = 0

def RestartNumberOfViewsInThisTestCase():
    global NumberOfViewsInThisTestCase
    NumberOfViewsInThisTestCase = 0

def RestartLenghtOfTestCase():
    global LenghtOfTestCase
    LenghtOfTestCase = 0

def AddLenghtOfTestCase():
    global LenghtOfTestCase
    LenghtOfTestCase = LenghtOfTestCase + 1


def AddNumberOfViewsInThisTestCase():
    global NumberOfViewsInThisTestCase
    NumberOfViewsInThisTestCase = NumberOfViewsInThisTestCase + 1


def AddNumberOfActionsInThisTestCase():
    global NumberOfActionsInThisTestCase
    NumberOfActionsInThisTestCase = NumberOfActionsInThisTestCase + 1


def getNumberOfActionsInThisTestCase():
    global NumberOfActionsInThisTestCase
    return NumberOfActionsInThisTestCase


def getNumberOfViewsInThisTestCase():
    global NumberOfViewsInThisTestCase
    return NumberOfViewsInThisTestCase


def getLenghtOfTestCase():
    global LenghtOfTestCase
    return LenghtOfTestCase


def getPossibleToRotate():
    global PossibleToRotate
    return PossibleToRotate


def setPossibleToRotate(r):
    global PossibleToRotate
    PossibleToRotate = r


def getPossibleToGoBackground():
    global PossibleToGoBackground
    return PossibleToGoBackground


def setPossibleToGoBackground(b):
    global PossibleToGoBackground
    PossibleToGoBackground = b


def getLeakDetection():
    global LeakDetection
    return LeakDetection


def setLeakDetection(l):
    global LeakDetection
    LeakDetection = l


def getActivity():
    global Activity
    return Activity


def setActivity(a):
    global Activity
    Activity = a


def getDesiredCap():
    global desired_caps
    return desired_caps


def setDesiredCap(d):
    global desired_caps
    desired_caps = d


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


def setActionCount(_actionCount):
    global ActionCount
    ActionCount = _actionCount
