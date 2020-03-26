from .BaseElement import BaseElement

class ImageView(BaseElement):

    def __init__(self, id, clickable, locationX, locationY):
        BaseElement.__init__(self, id, clickable, locationX, locationY)