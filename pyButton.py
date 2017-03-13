#Alejandro Hernandez
#pyButton.py [modified button class] (Final Project)
#December 18, 2013
#COM 110

#Purpose: Modified version of button class for the purpose
#of running and working the buttons on the PYphone
from graphics import *

class Button:
    """A labeled rectangle object in a graphics window,
    it can be activated or deactivated. Will also have
    a click method, which returns true if button is
    activated and point of mouse click is inside button"""

    def __init__(self, win, center, width, height, color):

        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x + width/2, x - width/2
        self.ymax, self.ymin = y + height/2, y - height/2

        p1 = Point(self.xmax, self.ymin)
        p2 = Point(self.xmin, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill(color)
        self.rect.setOutline(color)
        self.rect.draw(win)

        self.active = True

    def clicked(self, p):
        "Returns true if button active and Point p is inside"
        if self.active: #if active, check if the click is on the button
            if self.xmin<=p.getX()<=self.xmax and self.ymin<=p.getY()<=self.ymax:
                return True
            else: #if not...
                return False

    def undraw(self):
        """Button is now modified to undraw itself"""
        self.rect.undraw()

