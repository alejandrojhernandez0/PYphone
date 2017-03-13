#Alejandro Hernandez
#calculator.py (Final Project)
#December 18, 2013
#COM 110

#Purpose: Runs the calculator app on the PYphone, which takes
#user input to calculate simple equations.
from pyPhone import *

class calculator:

    def __init__(self,win):
        """Sets app to be run in the window"""

        self.win = win

    def showCalcMenu(self,win):
        """App Menu GUI is created"""

        #---STANDARD MENU GUI---
        self.Menu = Rectangle(Point(200,95),Point(425,500))
        self.Menu.setFill("black")
        self.Menu.setOutline("black")
        self.Menu.draw(self.win)

        self.allTxt = []
        self.allBut = []
        self.allEnt = []
        self.answer = ""
        
        self.Exit = Button(self.win,Point(230,125),30,20,"black")
        self.ExitImg = Image(Point(230,125),"icons/goback.gif")
        self.ExitImg.draw(self.win)
        #---STANDARD MENU GUI---

        self.txt = Text(Point(312.5,150),"Calculator")
        self.txt.setFill("limegreen")
        self.txt.setStyle("bold")
        self.txt.setSize(15)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.answerBox = Rectangle(Point(230,430),Point(400,460))
        self.answerBox.setFill("black")
        self.answerBox.setOutline("limegreen")
        self.answerBox.draw(self.win)
        self.txt = Text(Point(312.5,415),"Answer")
        self.txt.setFill("limegreen")
        self.txt.setStyle("bold")
        self.txt.setSize(12)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        #---INSTRUCTIONS GUI---
        self.txt = Text(Point(312.5,180),"Enter numbers in both entry boxes.")
        self.txt.setFill("limegreen")
        self.txt.setSize(9)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(312.5,200),"Then, click on the mathematical")
        self.txt.setFill("limegreen")
        self.txt.setSize(9)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(312.5,220),"operator that you want to use. It")
        self.txt.setFill("limegreen")
        self.txt.setSize(9)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(312.5,240),"will then display the answer in the")
        self.txt.setFill("limegreen")
        self.txt.setSize(9)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(312.5,260),"highlighted box under.")
        self.txt.setFill("limegreen")
        self.txt.setSize(9)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        #---INSTRUCTIONS GUI---

        #---NUMBERS PROMPT GUI---
        self.num1 = Entry(Point(230,325),5)
        self.num1.setFill("white")
        self.num1.draw(self.win)
        self.allEnt.append(self.num1)
        self.txt = Text(Point(230,280),"Enter 1st")
        self.txt.setFill("limegreen")
        self.txt.setSize(9)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        self.txt = Text(Point(230,300),"number")
        self.txt.setFill("limegreen")
        self.txt.setSize(9)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        
        self.num2 = Entry(Point(395,325),5)
        self.num2.setFill("white")
        self.num2.draw(self.win)
        self.allEnt.append(self.num2)
        self.txt = Text(Point(395,280),"Enter 2nd")
        self.txt.setFill("limegreen")
        self.txt.setSize(9)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        self.txt = Text(Point(395,300),"number")
        self.txt.setFill("limegreen")
        self.txt.setSize(9)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        #---NUMBERS PROMPT GUI---

        #---MATH OPERATIONS GUI---
        self.addB = Button(self.win,Point(282.5,300),40,40,"white")
        self.txt = Text(Point(282.5,300),"+")
        self.txt.setFill("black")
        self.txt.setSize(36)
        self.txt.draw(self.win)
        self.allBut.append(self.addB)
        self.allTxt.append(self.txt)
        
        self.subtractB = Button(self.win,Point(282.5,350),40,40,"white")
        self.txt = Text(Point(282.5,350),"-")
        self.txt.setFill("black")
        self.txt.setSize(36)
        self.txt.draw(self.win)
        self.allBut.append(self.subtractB)
        self.allTxt.append(self.txt)
        
        self.multiplyB = Button(self.win,Point(342.5,300),40,40,"white")
        self.txt = Text(Point(342.5,300),"X")
        self.txt.setFill("black")
        self.txt.setSize(36)
        self.txt.draw(self.win)
        self.allBut.append(self.multiplyB)
        self.allTxt.append(self.txt)
        
        self.divideB = Button(self.win,Point(342.5,350),40,40,"white")
        self.txt = Text(Point(342.5,350),"/")
        self.txt.setFill("black")
        self.txt.setSize(36)
        self.txt.draw(self.win)
        self.allBut.append(self.divideB)
        self.allTxt.append(self.txt)
        #---MATH OPERATIONS GUI---

    def hideCalcMenu(self):
        """All app Menu GUI is deleted after app is exited to main menu"""

        self.Menu.undraw()
        self.Exit.undraw()
        self.ExitImg.undraw()
        self.answerBox.undraw()

        for text in self.allTxt:
            text.undraw()

        for button in self.allBut:
            button.undraw()

        for entry in self.allEnt:
            entry.undraw()

    def ifCalcExitClicked(self,pt):
        """Checks if exit for app menu is clicked"""
        
        if(self.Exit.clicked(pt) == True):
            return True
        else:
            return False

    def ifAdd(self,pt):
        """Checks if add button is clicked"""
        
        if(self.addB.clicked(pt) == True):
            #Adds both entered numbers for answer that will be shown
            ans = int(self.num1.getText()) + int(self.num2.getText())
            ans = str(ans)
            self.answer = ans
            return True
        else:
            return False

    def ifSubtract(self,pt):
        """Checks if subtract button is clicked"""
        
        if(self.subtractB.clicked(pt) == True):
            #Subtracts both entered numbers for answer that will be shown
            ans = int(self.num1.getText()) - int(self.num2.getText())
            ans = str(ans)
            self.answer = ans
            return True
        else:
            return False

    def ifMultiply(self,pt):
        """Checks if multiply button is clicked"""
        
        if(self.multiplyB.clicked(pt) == True):
            #Multiplies both entered numbers for answer that will be shown
            ans = int(self.num1.getText()) * int(self.num2.getText())
            ans = str(ans)
            self.answer = ans
            return True
        else:
            return False

    def ifDivide(self,pt):
        """Checks if divide button is clicked"""
        
        if(self.divideB.clicked(pt) == True):
            #Divides the entered numbers for answer that will be shown
            ans = int(self.num1.getText()) / int(self.num2.getText())
            ans = str(ans)
            self.answer = ans
            return True
        else:
            return False

    def giveAnswer(self):
        """Does the prompt for the answer of the calculated equation"""

        #Shows the answer of the calculator equation as GUI text
        self.ans = Text(Point(315,445),self.answer)
        self.ans.setFill("limegreen")
        self.ans.draw(self.win)

        #Undraws the answer after 2 seconds for another user prompt to be entered
        sleep(2)
        self.ans.undraw()

        
