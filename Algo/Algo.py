from .LeakDetectionAlgo import LeakDetectionAlgo
from .ActionCoverageAlgo import ActionCoverageAlgo
from .StateCoverageAlgo import StateCoverageAlgo

def main(driver, currentView, algo, username, password):
    if username != "" and password != "":
        if ContainsUserName(currentView.getEditViewList(), username):
            if ContainsPassword(currentView.getEditViewList(), password):
                ClickLoginButton(currentView.getButtonViewList())

    if algo == "StateCoverage":
        StateCoverageAlgo()

    elif algo == "ActionCoverage":
        ActionCoverageAlgo()

    elif algo == "LeakDetection":
        LeakDetectionAlgo()


def ContainsUserName(editViewList, userName):
    for el in editViewList:
        if el.text.lower() == "username":
            el.click()
            el.send_keys(userName)
            return True
    return False


def ContainsPassword(editViewList, password):
    for el in editViewList:
        if el.text.lower() == "password":
            el.click()
            el.send_keys(password)
            return True
    return False


def ClickLoginButton(ButtonViewList):
    for el in ButtonViewList:
        if el.text.lower() == "login":
            el.click()