

class View(object):

    def __init__(self,id,ScreenShotLocation, ImageViewList, TextViewList, EditViewList, ButtonViewList):
        self.id = id
        self.ScreenShotLocation = ScreenShotLocation
        self.ImageViewList = ImageViewList
        self.TextViewList = TextViewList
        self.EditViewList = EditViewList
        self.ButtonViewList = ButtonViewList
        self.ParentViewID = None
        self.ChildView = []

    def getID(self):
        return self.id

    def getScreenShotLocation(self):
        return  self.ScreenShotLocation

    def getImageViewList(self):
        return  self.ImageViewList

    def getTextViewList(self):
        return  self.TextViewList

    def getEditViewList(self):
        return  self.EditViewList

    def getButtonViewList(self):
        return  self.ButtonViewList

    def getParentViewID(self):
        return self.ParentViewID

    def getChildView(self):
        return self.ChildView