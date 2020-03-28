from Algo.Helpers.ViewChecker import FindElements

driver = None
CurrentView = None

def ActionCoverageAlgo(_driver,_currentView):
    global driver, CurrentView
    driver = _driver
    CurrentView = _currentView
    ButtonListView = CurrentView.ButtonViewList
    EditViewList = CurrentView.EditViewList
    TextViewList = CurrentView.TextViewList
    ImageViewList = CurrentView.ImageViewList



    print("ActionCoverageAlgo")
