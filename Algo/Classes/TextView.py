from .BaseElement import BaseElement

class TextView(BaseElement):

    def __init__(self,id , clickable, locationX, locationY):
        BaseElement.__init__(self,id , clickable, locationX, locationY)