import GeometricFigure
import ColorOfFigure
import math

class Circ(GeometricFigure.GeoFig):
    def __init__(self, radius, color):
        self.radius = radius,
        self.color= color,
        r = ColorOfFigure.ColOfFig(self.color)
    def __set__(self, radius, color):
        self.radius = radius,
        self.color = color
    def Ploshad(self, radius):
        Pl = math.pi*radius[0]*2
        return Pl

    def __repr__(self):
        return "radius: {}, color: {}, square: {}".format(self.radius[0], self.color[0], self.Ploshad(self.radius))
    pass