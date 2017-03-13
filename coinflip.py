#Alejandro Hernandez
#coinflip.py (Final Project)
#December 18, 2013
#COM 110

#Purpose: Runs the Coin Flip app on the PYphone. This app is a game
#and the user is allowed to guess what the face of the "coin" will
#be when the game runs.
from pyPhone import *

class coinflip:

    def __init__(self,win):
        """Sets app to be run in the window"""

        self.win = win

    def showCoinMenu(self,win):
        """App Menu GUI is created"""

        #---STANDARD MENU GUI---
        self.Menu = Rectangle(Point(200,95),Point(425,500))
        self.Menu.setFill("brown")
        self.Menu.setOutline("brown")
        self.Menu.draw(self.win)

        self.Exit = Button(self.win,Point(230,125),30,20,"black")
        self.ExitImg = Image(Point(230,125),"icons/goback.gif")
        self.ExitImg.draw(self.win)
        #---STANDARD MENU GUI---
        
        self.choice = ""
        self.allTxt = []

        #---COIN IMAGE GUI---
        self.coin = Circle(Point(312.5,312.5),70)
        self.coin.setFill("gold")
        self.coin.setOutline("yellow")
        self.coin.draw(self.win)
        self.q = Text(Point(312.5,312.5),"?")
        self.q.setFill("black")
        self.q.setSize(36)
        self.q.draw(self.win)
        self.allTxt.append(self.q)
        #---COIN IMAGE GUI---
        
        #---BUTTON GUI---
        self.headsB = Button(self.win,Point(250,475),55,25,"white")
        self.txt = Text(Point(250,475),"HEADS")
        self.txt.setFill("black")
        self.txt.setStyle("bold")
        self.txt.setSize(11)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(312.5,475),"OR")
        self.txt.setFill("white")
        self.txt.setStyle("bold")
        self.txt.setSize(11)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        
        self.tailsB = Button(self.win,Point(375,475),55,25,"white")
        self.txt = Text(Point(375,475),"TAILS")
        self.txt.setFill("black")
        self.txt.setStyle("bold")
        self.txt.setSize(11)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        #---BUTTON GUI---

        #---INSTRUCTIONS GUI---
        self.txt = Text(Point(340,110),"Click on either the heads or tails button.")
        self.txt.setFill("white")
        self.txt.setSize(7)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(340,120),"The game will then run and the coin will")
        self.txt.setFill("white")
        self.txt.setSize(7)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(340,130),"be flipped. The actual face of the coin will")
        self.txt.setFill("white")
        self.txt.setSize(7)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(340,140),"be shown in red text. You win if your")
        self.txt.setFill("white")
        self.txt.setSize(7)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(340,150),"guess turns out to be correct.")
        self.txt.setFill("white")
        self.txt.setSize(7)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        #---INSTRUCTIONS GUI---

    def hideCoinMenu(self):
        """All app Menu GUI is deleted after app is exited to main menu"""

        self.Menu.undraw()
        self.Exit.undraw()
        self.ExitImg.undraw()
        self.headsB.undraw()
        self.tailsB.undraw()
        self.coin.undraw()

        for text in self.allTxt:
            text.undraw()

    def ifCoinExitClicked(self,pt):
        """Checks if exit for app menu is clicked"""
        
        if(self.Exit.clicked(pt) == True):
            return True
        else:
            return False

    def ifHeads(self,pt):
        """Checks if heads button is clicked"""
        
        if(self.headsB.clicked(pt) == True):
            self.choice = "heads"
            return True
        else:
            return False

    def ifTails(self,pt):
        """Checks if tails button is clicked"""
        
        if(self.tailsB.clicked(pt) == True):
            self.choice = "tails"
            return True
        else:
            return False

    def doGame(self):
        """Runs a new game of Coin Flip"""

        allTxt = []
        pos = [] #All possible choices (i.e. heads and tails)

        #All choices compiled in list
        heads = "HEADS"
        pos.append(heads)
        tails = "TAILS"
        pos.append(tails)

        answer = ""

        #Animated Text
        txt = Text(Point(312.5,450),"Running Game...")
        txt.setFill("white")
        txt.setSize(8)
        txt.draw(self.win)
        allTxt.append(txt)
        sleep(1)
        
        txt = Text(Point(312.5,405),"You guessed " + self.choice + ".")
        txt.setFill("white")
        txt.setStyle("bold")
        txt.setSize(10)
        txt.draw(self.win)
        allTxt.append(txt)
        sleep(1)

        txt = Text(Point(312.5,425),"Lets see if you guessed right...")
        txt.setFill("white")
        txt.setStyle("bold")
        txt.setSize(10)
        txt.draw(self.win)
        allTxt.append(txt)
        sleep(1)
        
        self.q.undraw()

        fpg = Text(Point(312.5,200),"Flipping...")
        fpg.setFill("white")
        fpg.setSize(8)
        fpg.draw(self.win)
        #Animated Text

        #Flip Animation
        x = 0
        while(x != 300):
            txt = Text(Point(312.5,312.5),pos[randrange(0,2)])
            txt.setFill("black")
            txt.setStyle("bold")
            txt.setSize(24)
            txt.draw(self.win)
            sleep(.001)
            txt.undraw()

            x += 1
        #Flip Animation

        fpg.undraw()
        sleep(2)

        #The correct face is chosen randomly
        r = randrange(0,2)
        correct = pos[r]

        face = Text(Point(312.5,312.5),correct)
        face.setFill("red")
        face.setStyle("bold")
        face.setSize(24)
        face.draw(self.win)
        allTxt.append(face)
        sleep(1)

        correct = correct.lower()

        #Says what the face of the coin is
        answer = Text(Point(312.5,180),"Its " + correct + "!")
        answer.setFill("white")
        answer.setStyle("bold")
        answer.setSize(14)
        answer.draw(self.win)
        allTxt.append(answer)
        sleep(1)

        #If you guessed right, this prompt is shown
        if(self.choice == correct):
            final = "You guessed right!"
            color = "green"

        #If your guess was wrong, this prompt is shown
        elif(self.choice != correct):
            final = "You guessed wrong."
            color = "black"

        #Gives out prompt and resets the game after for
        #another one to be run.
        Final = Text(Point(312.5,210),final)
        Final.setFill(color)
        Final.setStyle("bold")
        Final.setSize(14)
        Final.draw(self.win)
        allTxt.append(Final)
        sleep(3)
        
        #Reset to default config
        self.q.draw(self.win)

        for text in allTxt:
            text.undraw()
        #Reset to default config
            

        



        
            

        


        

        
