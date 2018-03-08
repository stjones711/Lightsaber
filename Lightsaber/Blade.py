from Graphics import *


class Blade(object):
    """creates a blade for the lightsaber"""

    def __init__(self, x, y, color, width, height, win):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height

    def drawBlade(self, win, x = 200, y = 250, color = "red", width = 200, height = 30):
        blade1 = Rectangle(Point(x, y), Point(x + width, y + height))
        blade1.setFill(color)
        blade1.setOutline("white")
        blade1.draw(win)


#win = GraphWin("Lightsaber", 1000, 650)
#win.setBackground("white")
