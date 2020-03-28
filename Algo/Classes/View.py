class View(object):

    def __init__(self, SelfID, ScreenShotLocation, ImageViewList, TextViewList, EditViewList, ButtonViewList):
        self.SelfID = SelfID
        self.ScreenShotLocation = ScreenShotLocation
        self.ImageViewList = ImageViewList
        self.TextViewList = TextViewList
        self.EditViewList = EditViewList
        self.ButtonViewList = ButtonViewList
        self.EverythingExecuted = False

    def getSelfID(self):
        return self.SelfID

    def getScreenShotLocation(self):
        return self.ScreenShotLocation

    def getImageViewList(self):
        return self.ImageViewList

    def getTextViewList(self):
        return self.TextViewList

    def getEditViewList(self):
        return self.EditViewList

    def getButtonViewList(self):
        return self.ButtonViewList
