#Alejandro Hernandez
#rockpaperscissors.py (Final Project)
#December 18, 2013
#COM 110

#Purpose: Runs the rock paper scissors game app on the PYphone. The user
#faces against the computer in a rock paper scissors battle where the user
#chooses their move against the computer. The computer's move is randomly
#generated.
from pyPhone import *

class rockpaperscissors:

    def __init__(self,win):
        """Sets app to be run in the window"""

        self.win = win

    def showRpsMenu(self,win):
        """App Menu GUI is created"""

        #---STANDARD MENU GUI---
        self.Menu = Rectangle(Point(200,95),Point(425,500))
        self.Menu.setFill("black")
        self.Menu.setOutline("black")
        self.Menu.draw(self.win)

        self.P_MOVE = ""
        self.allTxt = []

        self.Exit = Button(win,Point(230,125),30,20,"black")
        self.ExitImg = Image(Point(230,125),"icons/goback.gif")
        self.ExitImg.draw(self.win)
        #---STANDARD MENU GUI---

        #---BUTTON GUI---
        self.rockB = Button(self.win,Point(240,475),55,25,"blue")
        self.txt = Text(Point(240,475),"Rock")
        self.txt.setFill("white")
        self.txt.setStyle("bold")
        self.txt.setSize(10)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.paperB = Button(self.win,Point(312.5,475),55,25,"red")
        self.txt = Text(Point(312.5,475),"Paper")
        self.txt.setFill("white")
        self.txt.setStyle("bold")
        self.txt.setSize(10)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.scissorsB = Button(self.win,Point(385,475),55,25,"yellow")
        self.txt = Text(Point(385,475),"Scissors")
        self.txt.setFill("black")
        self.txt.setStyle("bold")
        self.txt.setSize(10)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        #---BUTTON GUI---

        self.txt = Text(Point(312.5,450),"Choose Your Attack:")
        self.txt.setFill("white")
        self.txt.setStyle("bold")
        self.txt.setSize(11)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        #---INSTRUCTIONS GUI---
        self.txt = Text(Point(340,110),"Click on 1 of the 3 buttons for your")
        self.txt.setFill("white")
        self.txt.setSize(7)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(340,120),"choice in the game, a game of rock")
        self.txt.setFill("white")
        self.txt.setSize(7)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(340,130),"paper scissors will then be run after.")
        self.txt.setFill("white")
        self.txt.setSize(7)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        #---INSTRUCTIONS GUI---
        

    def hideRpsMenu(self):
        """All app Menu GUI is deleted after app is exited to main menu"""

        self.Menu.undraw()
        self.Exit.undraw()
        self.ExitImg.undraw()
        
        self.rockB.undraw()
        self.paperB.undraw()
        self.scissorsB.undraw()

        for text in self.allTxt:
            text.undraw()

    def ifRpsExitClicked(self,pt):
        """Checks if exit for app menu is clicked"""
        
        if(self.Exit.clicked(pt) == True):
            return True
        else:
            return False

    def ifRock(self,pt):
        """Checks if rock button is clicked"""

        if(self.rockB.clicked(pt) == True):
            self.P_MOVE = "rock"
            return True
        else:
            return False

    def ifPaper(self,pt):
        """Checks if paper button is clicked"""

        if(self.paperB.clicked(pt) == True):
            self.P_MOVE = "paper"
            return True
        else:
            return False

    def ifScissors(self,pt):
        """Checks if scissors butoon is clicked"""

        if(self.scissorsB.clicked(pt) == True):
            self.P_MOVE = "scissors"
            return True
        else:
            return False

    def doGame(self):
        """Runs a new game of rock paper scissors"""

        #Stores all possible moves for computer
        AI_MOVE = ["rock","paper","scissors"]
        AI_RAND = randrange(0,3)

        allTxt = []

        #Prompts what move player chose
        txt = Text(Point(312.5,312.5),"You chose " + self.P_MOVE + ".")
        txt.setFill("white")
        txt.setStyle("bold")
        txt.setSize(12)
        txt.draw(self.win)
        sleep(2.5)
        txt.undraw()

        txt = Text(Point(312.5,425),"Running Game...")
        txt.setFill("white")
        txt.setSize(8)
        txt.draw(self.win)
        allTxt.append(txt)

        #Animation stuff
        txt = Text(Point(312.5,312.5),"Now get ready...")
        txt.setFill("white")
        txt.setStyle("bold")
        txt.setSize(12)
        txt.draw(self.win)
        sleep(2)
        txt.undraw()

        ROCK = Image(Point(312.5,260),"icons/rock.gif")
        ROCK.draw(self.win)
        txt = Text(Point(312.5,312.5),"Rock!")
        txt.setFill("blue")
        txt.setStyle("bold")
        txt.setSize(12)
        txt.draw(self.win)
        sleep(.35)
        ROCK.undraw()
        txt.undraw()

        PAPER = Image(Point(312.5,260),"icons/paper.gif")
        PAPER.draw(self.win)
        txt = Text(Point(312.5,312.5),"Paper!")
        txt.setFill("red")
        txt.setStyle("bold")
        txt.setSize(12)
        txt.draw(self.win)
        sleep(.35)
        PAPER.undraw()
        txt.undraw()

        SCISSORS = Image(Point(312.5,260),"icons/scissors.gif")
        SCISSORS.draw(self.win)
        txt = Text(Point(312.5,312.5),"Scissors!")
        txt.setFill("yellow")
        txt.setStyle("bold")
        txt.setSize(12)
        txt.draw(self.win)
        sleep(.35)
        SCISSORS.undraw()
        txt.undraw()

        txt = Text(Point(312.5,312.5),"Shoot!")
        txt.setFill("white")
        txt.setStyle("bold")
        txt.setSize(12)
        txt.draw(self.win)
        sleep(.35)
        txt.undraw()
        #Animation stuff

        #Shows images for either rock paper or scissors for both
        #the player and the computer
        P_IMG = Image(Point(312.5,360),"icons/"+self.P_MOVE+".gif")
        P_IMG.draw(self.win)

        D_IMG = Image(Point(312.5,200),"icons/"+AI_MOVE[AI_RAND]+".gif")
        D_IMG.draw(self.win)

        txt = Text(Point(390,360),"You")
        txt.setFill("white")
        txt.setSize(8)
        txt.draw(self.win)
        allTxt.append(txt)
        
        txt = Text(Point(390,200),"Computer")
        txt.setFill("white")
        txt.setSize(8)
        txt.draw(self.win)
        allTxt.append(txt)

        A_MOVE = AI_MOVE[AI_RAND]
        
        sleep(2)
        end = ""
        winner = ""

        #--------------------------------------
        #Decides who wins or loses depending
        #on the player and the computers choice
        #for the game
        if(self.P_MOVE == "rock"):
            if(A_MOVE == "paper"):
                end = "Paper covers rock."
                winner = "You Lose."
            elif(A_MOVE == "scissors"):
                end = "Rock crushes scissors."
                winner = "You Win!"
            elif(A_MOVE == "rock"):
                end = "Draw."
                winner = "Nobody Wins."
                
        elif(self.P_MOVE == "paper"):
            if(A_MOVE == "scissors"):
                end = "Scissors cuts paper."
                winner = "You Lose."
            elif(A_MOVE == "rock"):
                end = "Paper covers rock."
                winner = "You win."
            elif(A_MOVE == "paper"):
                end = "Draw."
                winner = "Nobody Wins."
                
        elif(self.P_MOVE == "scissors"):
            if(A_MOVE == "rock"):
                end = "Rock crushes scissors."
                winner = "You Lose."
            elif(A_MOVE == "paper"):
                end = "Scissors cuts paper."
                winner = "You Win."
            elif(A_MOVE == "scissors"):
                end = "Draw."
                winner = "Nobody Wins."
        #Decides who wins or loses depending
        #on the player and the computers choice
        #for the game
        #--------------------------------------

        #Prompts who wins, etc.
        txt = Text(Point(312.5,260),end)
        txt.setFill("white")
        txt.setStyle("bold")
        txt.setSize(12)
        txt.draw(self.win)
        allTxt.append(txt)
        
        txt = Text(Point(312.5,290),winner)
        txt.setFill("white")
        txt.setStyle("bold")
        txt.setSize(12)
        txt.draw(self.win)
        allTxt.append(txt)

        sleep(3)

        #Reset to default config
        P_IMG.undraw()
        D_IMG.undraw()

        for text in allTxt:
            text.undraw()
        #Reset to default config

        

        
        
        
        
