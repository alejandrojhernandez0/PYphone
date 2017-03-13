#Alejandro Hernandez
#internet.py (Final Project)
#December 18, 2013
#COM 110

#Runs the Internet app on the PYphone. User has the ability
#to type down a valid website and search for it, the PYphone
#will then open up on the computer internet browser.
from pyPhone import *
import webbrowser

class internet:

    def __init__(self,win):
        """Sets app to be run in the window"""

        self.win = win

    def showInternetMenu(self,win):
        """App Menu GUI is created"""

        #---STANDARD MENU GUI---
        self.Menu = Rectangle(Point(200,95),Point(425,500))
        self.Menu.setFill("lightgrey")
        self.Menu.setOutline("lightgrey")
        self.Menu.draw(self.win)

        self.allTxt = []
        self.allImg = []

        self.Exit = Button(self.win,Point(230,125),30,20,"black")
        self.ExitImg = Image(Point(230,125),"icons/goback.gif")
        self.ExitImg.draw(self.win)
        self.allImg.append(self.ExitImg)
        #---STANDARD MENU GUI---

        #---BUTTON AND ENTRY GUI---
        self.urlEnt = Entry(Point(312.5,312.5),20)
        self.urlEnt.setFill("white")
        self.urlEnt.draw(self.win)

        self.searchB = Button(self.win,Point(312.5,350),60,20,"darkblue")
        self.txt = Text(Point(312.5,350),"Search")
        self.txt.setFill("white")
        self.txt.setSize(13)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        #---BUTTON AND ENTRY GUI---

        self.img = Image(Point(312.5,200),"icons/internet.gif")
        self.img.draw(self.win)
        self.allImg.append(self.img)
        self.txt = Text(Point(312.5,250),"Internet Search")
        self.txt.setFill("darkgreen")
        self.txt.setSize(20)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        #---INSTRUCTIONS GUI---
        self.txt = Text(Point(312.5,380),"Instructions")
        self.txt.setFill("black")
        self.txt.setStyle("bold")
        self.txt.setSize(10)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        
        self.txt = Text(Point(312.5,400),"Please enter a valid website address")
        self.txt.setFill("black")
        self.txt.setSize(10)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(312.5,420),"in the entry box, then click on the")
        self.txt.setFill("black")
        self.txt.setSize(10)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(312.5,440),"search button. The website will then")
        self.txt.setFill("black")
        self.txt.setSize(10)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(312.5,460),"be opened on the computer")
        self.txt.setFill("black")
        self.txt.setSize(10)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(312.5,480),"internet browser.")
        self.txt.setFill("black")
        self.txt.setSize(10)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        #---INSTRUCTIONS GUI---

    def hideInternetMenu(self):
        """All app Menu GUI is deleted after app is exited to main menu"""

        self.Menu.undraw()
        self.Exit.undraw()
        self.ExitImg.undraw()
        self.urlEnt.undraw()
        self.searchB.undraw()

        for text in self.allTxt:
            text.undraw()

        for img in self.allImg:
            img.undraw()

    def ifInternetExitClicked(self,pt):
        """Checks if exit for app menu is clicked"""
        
        if(self.Exit.clicked(pt) == True):
            return True
        else:
            return False

    def ifSearchClicked(self,pt):
        """Checks if search button is clicked"""
        
        if(self.searchB.clicked(pt) == True):
            return True
        else:
            return False

    def doSearch(self):
        """Searches the website on the computer Internet browser"""
        
        webbrowser.open_new(self.urlEnt.getText())
        
