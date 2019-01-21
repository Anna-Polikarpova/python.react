import GeometricFigure
import ColorOfFigure

class Rect(GeometricFigure.GeoFig):
    def __init__(self, width, height, color):
        self.width = width,
        self.height = height,
        self.color = color,
        r = ColorOfFigure.ColOfFig(color)
    def __set__(self, width, height, color):
        self.width = width,
        self.height = height,
        self.color = color
    def Ploshad(self, width, height):
        Pl = width[0] * height[0]
        return Pl

    def __repr__(self):
        return "width: {}, height: {}, color: {}, square: {} ".format(self.width[0], self.height[0], self.color[0], self.Ploshad(self.width, self.height))
    pass