
class BaseElement(object):

    # Constructor
    def __init__(self,id , clickable, locationX, locationY):
        self.id = id
        self.tested = False
        self.clickable = clickable
        self.locationX = locationX
        self.locationY = locationY
        self.connectedView = None

    def getTested(self):
        return self.tested

    def getClickable(self):
        return self.clickable

    def getLocationX(self):
        return self.locationX

    def getLocationY(self):
        return self.locationY

    def getConnectedView(self):
        return self.connectedView