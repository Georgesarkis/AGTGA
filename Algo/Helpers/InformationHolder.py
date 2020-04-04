ActionCount = 0
Views = []
WaitTime = 0
count = 0
desired_caps = None
Activity = ""
LeakDetection = False
PossibleToRotate = True
PossibleToGoBackground = True


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
