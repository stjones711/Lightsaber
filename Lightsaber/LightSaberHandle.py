from Blade import *


class Handle(Blade):
    def __init__(self, x, y, width, height, color, win):
        super(Handle,self).__init__(x, y, width, height, color, win)
        self.drawHandle(win)
        self.drawButton(win)

    def drawHandle(self, x = 400, y = 250, color = "black"):
        hand = Rectangle(Point(x, y), Point(x + 225, y))
        hand.setFill(color)
        hand.draw(win)
        line = Line(Point(x + 30, y - 45), Point(x + 150, y - 65))
        line.setWidth(25)
        hand.draw(win)

    def drawButton(self, x, y):
        button = Circle(Point(x+255, y+ 485), 25)
        button.draw(win)


win = GraphWin("Lightsaber", 1000, 650)
win.setBackground("white")


blade2 = Blade(200, 250, "red", 200, 30, win)
blade2.drawBlade(200)
blade2.drawBlade(625)

handle = Handle(400, 250, 200, 30, "black", win)
handle.drawHandle()
handle.drawButton(100, 100)

win.getMouse()
win.close()




