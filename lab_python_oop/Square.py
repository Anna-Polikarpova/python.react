import Rectangle
import ColorOfFigure

class Squar(Rectangle.Rect):
    def __init__(self, length, color):
        self.length = length,
        self.color = color,
        r = ColorOfFigure.ColOfFig(self.color)
    def __set__(self, length, color):
        self.width = length,
        self.color = color
    def Ploshad(self, length):
        Pl = length[0]*length[0]
        return Pl

    def __repr__(self):
        return "length: {}, color: {}, square: {}".format(self.length[0], self.color[0], self.Ploshad(self.length))
    pass
