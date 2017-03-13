#Alejandro Hernandez
#diceroll.py (Final Project)
#December 18, 2013
#COM 110

#Purpose: Runs the dice roll app on the PYphone. User can play against
#the computer in a game of dice. Whoever has the highest value of dice
#wins.
from pyPhone import *
from dieview import *

class diceroll:

    def __init__(self,win):
        """Sets app to be run in the window"""

        self.win = win

    def showDiceMenu(self,win):
        """App Menu GUI is created"""

        #---STANDARD MENU GUI---
        self.Menu = Rectangle(Point(200,95),Point(425,500))
        self.Menu.setFill("darkgreen")
        self.Menu.setOutline("darkgreen")
        self.Menu.draw(self.win)

        self.Exit = Button(self.win,Point(230,125),30,20,"black")
        self.ExitImg = Image(Point(230,125),"icons/goback.gif")
        self.ExitImg.draw(self.win)
        #---STANDARD MENU GUI---

        self.allTxt = []

        #---DICE GUI---
        self.PDIE1 = DieView(self.win,Point(275,375),40)
        self.PDIE2 = DieView(self.win,Point(350,375),40)
        self.DDIE1 = DieView(self.win,Point(275,250),40)
        self.DDIE2 = DieView(self.win,Point(350,250),40)
        #---DICE GUI---

        self.txt = Text(Point(312.5,425),"Player")
        self.txt.setFill("white")
        self.txt.setSize(14)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        
        self.txt = Text(Point(312.5,200),"Computer")
        self.txt.setFill("white")
        self.txt.setSize(14)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        #---INSTRUCTIONS GUI---
        self.txt = Text(Point(340,110),"Click on roll button to play game,")
        self.txt.setFill("white")
        self.txt.setSize(7)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(340,120),"the game will then run and the dice will")
        self.txt.setFill("white")
        self.txt.setSize(7)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(340,130),"then be rolled. Whoever has the highest")
        self.txt.setFill("white")
        self.txt.setSize(7)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(340,140),"dice value wins the game.")
        self.txt.setFill("white")
        self.txt.setSize(7)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        #---INSTRUCTIONS GUI---

        #---Button GUI---
        self.rollB = Button(self.win,Point(312.5,475),55,25,"black")
        self.txt = Text(Point(312.5,475),"ROLL")
        self.txt.setFill("white")
        self.txt.setStyle("bold")
        self.txt.setSize(12)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        #---Button GUI---

    def hideDiceMenu(self):
        """All app Menu GUI is deleted after app is exited to main menu"""

        self.Menu.undraw()
        self.Exit.undraw()
        self.ExitImg.undraw()
        
        self.PDIE1.undraw()
        self.PDIE2.undraw()
        self.DDIE1.undraw()
        self.DDIE2.undraw()

        self.rollB.undraw()

        for text in self.allTxt:
            text.undraw()

    def ifDiceExitClicked(self,pt):
        """Checks if exit for app menu is clicked"""
        
        if(self.Exit.clicked(pt) == True):
            return True
        else:
            return False

    def ifRoll(self,pt):
        """Check if roll button is clicked"""
        
        if(self.rollB.clicked(pt) == True):
            return True
        else:
            return False

    def doGame(self):
        """Runs a new game of Dice Roll"""

        #Randomizes the dice value for each oppponent
        PVAL1 = randrange(1,7)
        PVAL2 = randrange(1,7)
        DVAL1 = randrange(1,7)
        DVAL2 = randrange(1,7)

        allText = []
        winner = ""

        txt = Text(Point(312.5,450),"Running Game...")
        txt.setFill("white")
        txt.setSize(8)
        txt.draw(self.win)
        allText.append(txt)
        sleep(.02)

        #Sets the randomized dice values to player and the computer
        #on the dice GUI
        self.PDIE1.setValue(PVAL1)
        self.PDIE2.setValue(PVAL2)
        sleep(1)
        self.DDIE1.setValue(DVAL1)
        self.DDIE2.setValue(DVAL2)
        sleep(1)

        #Dice values are added
        PTOTAL = PVAL1 + PVAL2
        DTOTAL = DVAL1 + DVAL2

        #Shows value of player's dice in GUI
        PSCORE_C = Circle(Point(400,375),15)
        PSCORE_C.setFill("red")
        PSCORE_C.setOutline("red")
        PSCORE_C.draw(self.win)
        PSCORE_T = Text(Point(400,375),str(PTOTAL))
        PSCORE_T.setFill("white")
        PSCORE_T.setStyle("bold italic")
        PSCORE_T.setSize(12)
        PSCORE_T.draw(self.win)
        allText.append(PSCORE_T)

        #Shows value of computer's dice in GUI
        DSCORE_C = Circle(Point(400,250),15)
        DSCORE_C.setFill("red")
        DSCORE_C.setOutline("red")
        DSCORE_C.draw(self.win)
        DSCORE_T = Text(Point(400,250),str(DTOTAL))
        DSCORE_T.setFill("white")
        DSCORE_T.setStyle("bold italic")
        DSCORE_T.setSize(12)
        DSCORE_T.draw(self.win)
        allText.append(DSCORE_T)

        sleep(1)

        #Decides who won the game
        if(PTOTAL > DTOTAL):
            winner = "Player Wins!"
        elif(PTOTAL < DTOTAL):
            winner = "Computer Wins!"
        elif(PTOTAL == DTOTAL):
            winner = "Tie."

        #Prompts who won the game, the game will reset
        #seconds after this prompt is shown for more new
        #games to be run
        output = Text(Point(312.5,312.5),winner)
        output.setFill("white")
        output.setStyle("bold")
        output.setSize(12)
        output.draw(self.win)
        allText.append(output)

        sleep(3)

        #Reset to default config
        PSCORE_C.undraw()
        DSCORE_C.undraw()

        for text in allText:
            text.undraw()

        self.PDIE1.setValue(1)
        self.PDIE2.setValue(1)
        self.DDIE1.setValue(1)
        self.DDIE2.setValue(1)
        #Reset to default config

        
        



        
