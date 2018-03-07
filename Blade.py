from Graphics import *


class Blade(object):
    """creates a blade for the lightsaber"""

    def __init__(self, x, y, color, width, height, win):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height

    def drawBlade(x, y, color, width = 200, height = 30):
        blade = Rectangle(Point(x, y), Point(x + width, y + height))
        blade.setFill(color)
        blade.setOutline("white")
        blade.draw(win)


    def main(win):
        """Runs the main code"""
        Blade.drawBlade(200, 250, "red")
        Blade.drawBlade(625, 250, "red")




        win.getMouse()
        win.close()



win = GraphWin("Lightsaber", 1000, 650)
win.setBackground("black")

Blade.main(win)